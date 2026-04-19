from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Amber_Diceless_Sean_GURPS_3e_Adaptation" / "GURPS AMBER Role-Playing In the world of Roger Zelazny's Amber.html"


@dataclass(frozen=True)
class Target:
    out_file: Path
    css_href: str
    home_href: str
    reference_href: str
    session_href: str
    pdf_href: str
    cover_src: str


TARGETS = [
    Target(
        out_file=ROOT / "thread_clean_reader_site" / "amber_diceless" / "GURPS_Amber_Sean_Grinslade_1993.html",
        css_href="../thread_style.css",
        home_href="../index.html",
        reference_href="../01a_reference_gallery.html",
        session_href="../01_session_01.html#amber-gurps-1993",
        pdf_href="Amber_Diceless_RPG_Phage_Press.pdf",
        cover_src="Amber_Diceless_RPG_Cover.jpg",
    ),
    Target(
        out_file=ROOT / "FRH_HTML_Reader" / "content" / "amber_diceless" / "GURPS_Amber_Sean_Grinslade_1993.html",
        css_href="../../assets/css/thread_style.css",
        home_href="../../index.html",
        reference_href="../01a_reference_gallery.html",
        session_href="../01_session_01.html#amber-gurps-1993",
        pdf_href="Amber_Diceless_RPG_Phage_Press.pdf",
        cover_src="../../assets/images/Amber_Diceless_RPG_Cover.jpg",
    ),
]


MOJIBAKE_FIXES = {
    "â€œ": "“",
    "â€": "”",
    "â€?": "”",
    "â€™": "’",
    "â€˜": "‘",
    "â€¦": "…",
    "â€“": "–",
    "â€”": "—",
    "Â ": " ",
}


OCR_FIXES = {
    "litle less": "little less",
    "will mere novices": "will be mere novices",
    "shadow your in": "shadow you're in",
    "skillevel": "skill level",
    "prereg": "prereq",
    "Prereg": "Prereq",
    "A/l Advanced": "All Advanced",
    "Iinternal": "Internal",
    "durabilily": "durability",
    "ltems empowered": "Items empowered",
    "Ssing actual": "Using actual",
    "become resistance 1to change": "become resistant to change",
    "ensorcelment": "ensorcellment",
    "recelve": "receive",
    "Time FIow": "Time Flow",
    "(M7H)": "(M/H)",
    "(WVH)": "(M/VH)",
    "(MH)": "(M/H)",
}


TOC = [
    ("Introduction", "intro"),
    ("Basic Amber Package", "basic-amber-package"),
    ("Powers", "powers"),
    ("Pattern", "pattern"),
    ("Logrus", "logrus"),
    ("Trump", "trump"),
    ("Shapeshifting", "shapeshifting"),
    ("Magic", "magic"),
    ("Power Words", "power-words"),
    ("Creations", "creations"),
    ("Shadows", "shadows"),
]


def fix_mojibake(text: str) -> str:
    for bad, good in MOJIBAKE_FIXES.items():
        text = text.replace(bad, good)
    return text


def fix_ocr_artifacts(text: str) -> str:
    for bad, good in OCR_FIXES.items():
        text = text.replace(bad, good)
    text = re.sub(r"become resistance\s+1to\s+change", "become resistant to change", text)
    return text


def strip_export_noise(body: str) -> str:
    body = re.sub(r"<a\s+name=\"[^\"]*\"></a>", "", body, flags=re.I)
    body = re.sub(r"</?font\b[^>]*>", "", body, flags=re.I)
    body = re.sub(r"</?span\b[^>]*>", "", body, flags=re.I)
    body = re.sub(r"<col\b[^>]*>", "", body, flags=re.I)
    body = re.sub(
        r"\s(?:style|width|height|align|valign|border|cellpadding|cellspacing|bgcolor|link|vlink|dir|lang)=\"[^\"]*\"",
        "",
        body,
        flags=re.I,
    )
    body = re.sub(r"<p>\s*(?:<br\s*/?>\s*)+</p>", "", body, flags=re.I)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def remove_export_title(body: str) -> str:
    # The first three paragraph blocks are a blank spacer, the title, and the byline.
    for _ in range(3):
        body = re.sub(r"^\s*<p\b[^>]*>.*?</p>\s*", "", body, count=1, flags=re.S | re.I)
    return body


def add_section_structure(body: str) -> str:
    body = re.sub(
        r"<p>\s*GURPS AMBER\s+ROLE-PLAYING\s*</p>",
        '<h2 id="intro">GURPS Amber Role-Playing</h2>',
        body,
        count=1,
        flags=re.I,
    )
    body = re.sub(
        r"<p>\s*(?:<br\s*/?>\s*)?BASIC AMBER\s+PACKAGE\s*</p>",
        '<h2 id="basic-amber-package">Basic Amber Package</h2>',
        body,
        count=1,
        flags=re.I,
    )
    body = re.sub(
        r"<br\s*/?>\s*POWERS\s*<br\s*/?>\s*The Pattern\s*\(200 points\)\s*<br\s*/?>",
        '<h2 id="powers">Powers</h2><h3 id="pattern">The Pattern (200 points)</h3>',
        body,
        count=1,
        flags=re.I,
    )
    replacements = [
        (r"The Logrus\s*\(150\s+points\)", '<h3 id="logrus">The Logrus (150 points)</h3>'),
        (r"Trump\s*<br\s*/?>\s*Trumps are", '<h3 id="trump">Trump</h3>Trumps are'),
        (r"Shapeshifting\s*<br\s*/?>", '<h3 id="shapeshifting">Shapeshifting</h3>'),
        (r"MAGIC\s*<br\s*/?>", '<h3 id="magic">Magic</h3>'),
        (r"Power Words\s*\(20\s*<br\s*/?>\s*points\)", '<h3 id="power-words">Power Words (20 points)</h3>'),
        (r"How to Build a Creation in Five Easy Steps", '<h2 id="creations">How to Build a Creation in Five Easy Steps</h2>'),
        (r"<p>\s*SHADOWS\s*(?:<br\s*/?>)?\s*</p>", '<h2 id="shadows">Shadows</h2>'),
    ]
    for pattern, repl in replacements:
        body = re.sub(pattern, repl, body, count=1, flags=re.I)
    return body


def add_flow_section_structure(body: str) -> str:
    body = re.sub(
        r"<p>\s*POWERS\s+The\s+Pattern\s*\(200 points\)\s+",
        '<h2 id="powers">Powers</h2>\n<h3 id="pattern">The Pattern (200 points)</h3>\n<p>',
        body,
        count=1,
        flags=re.I,
    )
    body = re.sub(
        r"Trump\s+Artistry\s*\(120 points\)\s+Trumps are",
        '<h3 id="trump">Trump Artistry (120 points)</h3>Trumps are',
        body,
        count=1,
        flags=re.I,
    )
    body = re.sub(
        r"<p>\s*Power Words\s*\(20\s*points\)\s*-\s*",
        '<h3 id="power-words">Power Words (20 points)</h3>\n<p>',
        body,
        count=1,
        flags=re.I,
    )
    body = re.sub(
        r"\s+Power Words\s*\(20\s*points\)\s+This is",
        '</p>\n<h3 id="power-words">Power Words (20 points)</h3>\n<p>This is',
        body,
        count=1,
        flags=re.I,
    )
    body = re.sub(
        r"<p>\s*How to Build a\s+Creation in Five Easy Steps\s+",
        '<h2 id="creations">How to Build a Creation in Five Easy Steps</h2>\n<p>',
        body,
        count=1,
        flags=re.I,
    )
    body = re.sub(
        r"<p>\s*SHADOWS\s*</p>",
        '<h2 id="shadows">Shadows</h2>',
        body,
        count=1,
        flags=re.I,
    )
    return body


def clean_body() -> str:
    raw = SOURCE.read_text(encoding="utf-8", errors="ignore")
    raw = fix_mojibake(raw)
    match = re.search(r"<body[^>]*>(.*)</body>", raw, flags=re.S | re.I)
    if not match:
        raise ValueError(f"No body found in {SOURCE}")
    body = remove_export_title(match.group(1))
    body = strip_export_noise(body)
    body = add_section_structure(body)
    body = re.sub(r"<br\s*/?>\s*", " ", body, flags=re.I)
    body = re.sub(r"\s+</p>", "</p>", body)
    body = add_flow_section_structure(body)
    body = fix_ocr_artifacts(body)
    body = body.replace("<table>", '<div class="table-scroll"><table>')
    body = body.replace("</table>", "</table></div>")
    return body


def page_html(target: Target, body: str) -> str:
    nav = (
        f'<a href="{html.escape(target.home_href)}">Reader Home</a> | '
        f'<a href="{html.escape(target.reference_href)}">Reference Gallery</a> | '
        f'<a href="{html.escape(target.session_href)}">Session 1 Discussion</a> | '
        f'<a href="{html.escape(target.pdf_href)}">Amber Diceless PDF</a>'
    )
    toc_links = "\n".join(f'          <a href="#{anchor}">{html.escape(label)}</a>' for label, anchor in TOC)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GURPS Amber - Sean Grinslade 1993 Adaptation</title>
  <link rel="stylesheet" href="{html.escape(target.css_href)}">
</head>
<body class="legacy-page amber-adaptation-page">
  <main class="legacy-main amber-main">
    <p class="part">Amber Diceless Reference</p>
    <div class="nav">
      <p>{nav}</p>
    </div>

    <header class="amber-hero">
      <img src="{html.escape(target.cover_src)}" alt="Amber Diceless Role-Playing cover">
      <div>
        <h1>GURPS Amber</h1>
        <p class="deck">Role-Playing in the world of Roger Zelazny's Amber</p>
        <p>Adapted by Sean Grinslade from the Amber Dice-less Role-Playing Game by Eric Wujcik.</p>
      </div>
    </header>

    <nav class="amber-toc" aria-label="GURPS Amber sections">
      <h2>On This Page</h2>
      <div>
{toc_links}
      </div>
    </nav>

    <article class="legacy-article amber-adaptation">
{body}
    </article>

    <div class="page-footer">
      <div class="chapter-nav">
        <a href="{html.escape(target.reference_href)}">Reference Gallery</a>
        <a class="primary" href="{html.escape(target.session_href)}">Session 1 Discussion</a>
        <a href="{html.escape(target.home_href)}">Reader Home</a>
      </div>
      <p class="footer-note">This page is a cleaned reader presentation of the original 1993 Writer/WinWord export.</p>
    </div>
  </main>
</body>
</html>
"""


def main() -> None:
    body = clean_body()
    for target in TARGETS:
        target.out_file.parent.mkdir(parents=True, exist_ok=True)
        target.out_file.write_text(page_html(target, body), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
