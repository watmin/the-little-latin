"""MkDocs hook: question-group bookmarks + section mottos for The Little Latin.

Markdown conventions (see notes/STATE.md):
  Group marker (own line, directly above a Question|Answer table):
      {#g-03}
      -> a tappable bookmark badge with id="g-03".
  Motto line: :: Latin motto || English gloss
      -> a styled motto block (Latin, then a small italic gloss).
"""
import html
import re

GROUP = re.compile(r"^\{#(g-(\d{2}[a-z]*))\}[ \t]*$", re.M)
MOTTO = re.compile(r"^:: (.+?) \|\| (.+)$", re.M)


COVER = re.compile(r'^::: cover ([a-z0-9-]+) "([^"]+)" (shown|hidden)[ \t]*\n(.*?)\n:::[ \t]*$', re.M | re.S)


DIALOGUE = re.compile(r"^::: dialogue ([a-z0-9-]+)[ \t]*\n(.*?)\n:::[ \t]*$", re.M | re.S)


def _inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)


def _dialogue(m):
    rows = []
    for i, line in enumerate(l for l in m[2].split("\n") if l.strip()):
        la, en = [x.strip() for x in line.split("||", 1)]
        (sl, tl), (se, te) = [[y.strip() for y in x.split("|", 1)] for x in (la, en)]
        rows.append(
            f'<div class="dlg-line" data-line="{i}">'
            f'<div class="dlg-la" lang="la"><span class="dlg-who">{_inline(sl)}:</span> {_inline(tl)}</div>'
            f'<div class="dlg-en" lang="en"><span class="dlg-who">{_inline(se)}:</span> {_inline(te)}</div></div>'
        )
    head = '<div class="dlg-head" aria-hidden="true"><div>Latīna</div><div>Anglica</div></div>'
    return f'<div class="tll-dialogue" data-dlg-id="{m[1]}">' + head + "".join(rows) + "</div>"


def on_page_markdown(markdown, **kwargs):
    # Interleaved dialogue:  ::: dialogue <id>  /  Speaker | Latin || Speaker | English  /  :::
    markdown = DIALOGUE.sub(_dialogue, markdown)
    # Coverable block:  ::: cover <id> "<label>" shown|hidden  ...  :::
    markdown = COVER.sub(
        lambda m: f'<div class="tll-cover" data-cover-id="{m[1]}" data-label="{html.escape(m[2])}" '
        f'data-default="{m[3]}" markdown="1">\n\n{m[4]}\n\n</div>',
        markdown,
    )
    markdown = GROUP.sub(
        lambda m: f'<p class="group-mark"><a class="group-id" id="{m[1]}" href="#{m[1]}" '
        f'title="Bookmark this group of questions">🔖 {m[2]}</a></p>\n',
        markdown,
    )
    markdown = MOTTO.sub(
        lambda m: f'<p class="motto"><span class="motto-la">{html.escape(m[1])}</span>'
        f'<br><span class="motto-gloss">{html.escape(m[2])}</span></p>',
        markdown,
    )
    return markdown


# Cache-busting: append ?v=<content hash> to our own CSS/JS so phones never mix stale assets.
import hashlib
import os

_ASSETS = ("stylesheets/extra.css", "javascripts/extra.js", "javascripts/cards.js")
_HASHES = {}


def on_config(config, **kwargs):
    for a in _ASSETS:
        p = os.path.join(config["docs_dir"], a)
        with open(p, "rb") as f:
            _HASHES[a] = hashlib.sha1(f.read()).hexdigest()[:10]
    return config


def on_post_page(output, **kwargs):
    for a, h in _HASHES.items():
        output = re.sub(re.escape(a) + r'(?=")', f"{a}?v={h}", output)
    return output


# ---------------------------------------------------------------------------
# Tabellae (cards): collect docs/liber-*/cards/*.yml, validate, emit cards.json,
# generate per-book quiz pages + nav entries, append a chapter quiz section.
# Design: notes/consilia/2026/10/27/001-cards-design.md
import glob
import json

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File
from mkdocs.structure.nav import Section
from mkdocs.structure.pages import Page

ROMAN = ["i", "ii", "iii", "iv", "v", "vi"]
TYPES = {"vocab": ("la", "en"), "forms": ("q", "a"), "choose": ("q", "options", "a", "why"), "error": ("q", "a")}
QUIZ = re.compile(r"^::: quiz (all|book ([a-z]+)|chapter ([a-z]+) (\d+))[ \t]*$", re.M)
_CARDS = {"chapters": [], "cards": []}
_CH_FILES = {}  # page src path -> (book, ch)


def _plain(t):
    return t.replace("*", "").strip()


def _load_cards(docs_dir):
    errs, seen, chapters, cards = [], set(), [], []
    for path in sorted(glob.glob(os.path.join(docs_dir, "liber-*", "cards", "*.yml"))):
        rel = os.path.relpath(path, docs_dir)
        with open(path, encoding="utf-8") as f:
            d = yaml.safe_load(f)
        book, ch, page = d.get("book"), d.get("ch"), d.get("page")
        pp = os.path.join(docs_dir, page or "")
        if book not in ROMAN or not isinstance(ch, int) or not page or not os.path.exists(pp):
            errs.append(f"{rel}: bad book/ch/page header"); continue
        with open(pp, encoding="utf-8") as f:
            md = f.read()
        title = re.search(r"^# (.+)$", md, re.M)[1]
        groups = set(m[1] for m in GROUP.finditer(md))
        vocab = set()
        if "## Vocābula" in md:
            for line in md.split("## Vocābula", 1)[1].split("\n## ", 1)[0].splitlines():
                m = re.match(r"^\| \*([^*]+)\*", line)
                if m: vocab.add(m[1].strip())
        key = f"{book}-{ch:02d}"
        prefix = f"{book}{ch:02d}-"
        chapters.append({"key": key, "book": book, "ch": ch, "title": title,
                         "url": page[:-3] + "/"})
        _CH_FILES[page] = (book, ch)
        for c in d.get("cards") or []:
            cid, ty = c.get("id"), c.get("type")
            where = f"{rel}: {cid}"
            if not cid or cid in seen: errs.append(f"{where}: missing or duplicate id"); continue
            seen.add(cid)
            if not cid.startswith(prefix): errs.append(f"{where}: id must start with {prefix}")
            if ty not in TYPES: errs.append(f"{where}: unknown type {ty}"); continue
            for k in TYPES[ty] + ("ref",):
                if not c.get(k): errs.append(f"{where}: missing {k}")
            if c.get("ref") and c["ref"] not in groups: errs.append(f"{where}: ref {c.get('ref')} not in page")
            if ty == "choose" and c.get("a") not in (c.get("options") or []): errs.append(f"{where}: answer not among options")
            if ty == "vocab" and c.get("la") not in vocab: errs.append(f"{where}: '{c.get('la')}' not in Vocābula table")
            out = {"id": cid, "type": ty, "key": key, "ref": page[:-3] + "/#" + str(c.get("ref"))}
            if ty == "vocab":
                out["la"], out["en"] = _inline(c["la"]), _inline(c["en"])
            else:
                q = c["q"]
                if ty == "choose":
                    q += "  (" + " · ".join(f"*{o}*" for o in c["options"]) + ")"
                    a = f"*{c['a']}*. {c['why']}"
                else:
                    a = c["a"] + (f" {c['why']}" if c.get("why") else "")
                out["q"], out["a"] = _inline(q), _inline(a)
            cards.append(out)
    if errs:
        raise PluginError("Card validation failed:\n  " + "\n  ".join(errs))
    _CARDS["chapters"], _CARDS["cards"] = chapters, cards


def _book_pages():
    return sorted({c["book"] for c in _CARDS["chapters"]}, key=ROMAN.index)


def on_files(files, config, **kwargs):
    _load_cards(config["docs_dir"])
    for b in _book_pages():
        src = f"liber-{b}/tabellae.md"
        if not files.get_file_from_path(src):
            content = (f"# Tabellae: Liber {b.upper()}\n\n"
                       f"*Cards from every chapter of Liber {b.upper()}. Refresh for a new round.*\n\n"
                       f"::: quiz book {b}\n")
            files.append(File.generated(config, src, content=content))
    return files


def on_nav(nav, config, files, **kwargs):
    for b in _book_pages():
        f = files.get_file_from_path(f"liber-{b}/tabellae.md")
        for item in nav.items:
            if isinstance(item, Section) and item.title.startswith(f"Liber {b.upper()}:"):
                page = Page("Tabellae", f, config)
                page.parent = item
                item.children.append(page)
    return nav


def _quiz(m):
    if m[1] == "all":
        attrs = 'data-scope="all"'
    elif m[2]:
        attrs = f'data-scope="book" data-book="{m[2]}"'
    else:
        attrs = f'data-scope="chapter" data-book="{m[3]}" data-ch="{int(m[4])}"'
    return f'<div class="tll-quiz" data-no-persist {attrs}><p class="tll-quiz-loading">Tabellae parantur… (loading cards)</p></div>'


def _chapter_quiz_section(markdown, page):
    bc = _CH_FILES.get(page.file.src_uri)
    if not bc or "::: quiz" in markdown:
        return markdown
    return markdown.rstrip() + (
        "\n\n## Tabellae\n\n:: Ūsus magister est optimus. || Practice is the best teacher. (proverb)\n\n"
        "Twenty random cards from this chapter only. Say the answer aloud, then tap. Refresh for a new round.\n\n"
        f"::: quiz chapter {bc[0]} {bc[1]}\n")


_orig_page_markdown = on_page_markdown


def on_page_markdown(markdown, page=None, **kwargs):  # noqa: F811
    if page is not None:
        markdown = _chapter_quiz_section(markdown, page)
    markdown = QUIZ.sub(_quiz, markdown)
    return _orig_page_markdown(markdown, page=page, **kwargs)


def on_post_build(config, **kwargs):
    with open(os.path.join(config["site_dir"], "cards.json"), "w", encoding="utf-8") as f:
        json.dump(_CARDS, f, ensure_ascii=False, separators=(",", ":"))
