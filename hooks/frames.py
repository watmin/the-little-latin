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


def on_page_markdown(markdown, **kwargs):
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
