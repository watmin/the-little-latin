"""MkDocs hook: frame permalinks + section mottos for The Little Latin.

Markdown conventions (see notes/STATE.md):
  Frame row:  | {#f-012} Question text | Answer |
      -> the question cell gets a tappable anchor "012" with id="f-012".
  Motto line: :: Latin motto || English gloss
      -> a styled motto block (Latin, then a small italic gloss).
"""
import html
import re

FRAME = re.compile(r"^\| \{#(f-(\d{3}[a-z]*))\} ", re.M)
MOTTO = re.compile(r"^:: (.+?) \|\| (.+)$", re.M)


def on_page_markdown(markdown, **kwargs):
    markdown = FRAME.sub(
        lambda m: f'| <a class="frame-id" id="{m[1]}" href="#{m[1]}" title="Link to this frame">{m[2]}</a> ',
        markdown,
    )
    markdown = MOTTO.sub(
        lambda m: f'<p class="motto"><span class="motto-la">{html.escape(m[1])}</span>'
        f'<br><span class="motto-gloss">{html.escape(m[2])}</span></p>',
        markdown,
    )
    return markdown
