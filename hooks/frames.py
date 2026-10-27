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

_ASSETS = ("stylesheets/extra.css", "javascripts/extra.js")
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
