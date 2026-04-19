from __future__ import annotations

import html
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "FRH_New_Player_Packet_Beta_v1.3"

GURPS_LITE_URL = (
    "https://warehouse23.com/products/gurps-lite-third-edition"
    "?_gl=1%2Agib45h%2A_ga%2ANjk3MDgzMDc2LjE3NzE2NzQwNzQ."
    "%2A_ga_BZNY1LRRWR%2AczE3NzY1ODEzOTgkbzckZzAkdDE3NzY1ODEzOTgkajYwJGwwJGgw"
)


@dataclass(frozen=True)
class Target:
    root: Path
    css_href: str
    char_css_href: str
    char_image_prefix: str
    home_href: str
    char_home_href: str
    reference_href: str
    intro_href: str
    edgar_letter_href: str


TARGETS = [
    Target(
        ROOT / "thread_clean_reader_site" / "npp",
        "../thread_style.css",
        "../../thread_style.css",
        "../../",
        "../index.html",
        "../../index.html",
        "../01a_reference_gallery.html",
        "../00_intro_and_setup.html#npp",
        "../Edgar_Von_Haupt_Letter.html",
    ),
    Target(
        ROOT / "FRH_HTML_Reader" / "content" / "npp",
        "../../assets/css/thread_style.css",
        "../../../assets/css/thread_style.css",
        "../../../assets/images/",
        "../index.html",
        "../../index.html",
        "../01a_reference_gallery.html",
        "../00_intro_and_setup.html#npp",
        "../Edgar_Von_Haupt_Letter.html",
    ),
]


DOCS = [
    {
        "title": "Edgar Von Haupt Letter",
        "slug": "edgar-von-haupt-letter",
        "source": SOURCE / "01_Edgar Von Haupt Letter_beta_v1.1.md",
        "section": "Core Packet",
        "desc": "The in-world invitation that opens the packet and sets the tone for the campaign.",
    },
    {
        "title": "Character Creation Guide",
        "slug": "character-creation-guide",
        "source": SOURCE / "02_Character_Creation_Guide_FRH_Expanded_beta_v2.4.docx",
        "section": "Core Packet",
        "desc": "How to build an FRH investigator and understand the campaign's character expectations.",
    },
    {
        "title": "Cloudburg Overview",
        "slug": "cloudburg-overview",
        "source": SOURCE / "03_Cloudburg_Final.v1.0.docx",
        "section": "Core Packet",
        "desc": "A player-facing introduction to Cloudburg and its local campaign pressure.",
    },
    {
        "title": "Tiberius Example Play-Through",
        "slug": "tiberius-example-playthrough",
        "source": SOURCE / "05_Tiberius_Example_Playthrough_final.docx",
        "section": "Core Packet",
        "desc": "A worked example showing how FRH play unfolds through investigation and consequence.",
    },
    {
        "title": "Pregenerated Character Mechanics Overview",
        "slug": "pregenerated-character-mechanics-overview",
        "source": SOURCE / "04_Pre-generated_Character_Mechanics_Overview_beta_v4.2.docx",
        "section": "Core Packet",
        "desc": "A guide to the included pregenerated characters and what their mechanics demonstrate.",
    },
    {
        "title": "FRH Flyer",
        "slug": "frh-flyer",
        "source": SOURCE / "FHR_Flyer_beta_v1.3.docx",
        "section": "Core Packet",
        "desc": "A short campaign-facing flyer for the premise and invitation.",
    },
    {
        "title": "Advanced Optional Appendix",
        "slug": "advanced-optional-appendix",
        "source": SOURCE / "Advanced_Appendix" / "Advanced_Optional_Appendix._beta_v1.docx",
        "section": "Advanced Appendix",
        "desc": "Supplementary material for readers who want more examples after the main packet.",
    },
    {
        "title": "Tiberius Case Study Framing",
        "slug": "tiberius-case-study-framing",
        "source": SOURCE / "Advanced_Appendix" / "Tiberius_Case_Study_Framing.v1.1.docx",
        "section": "Advanced Appendix",
        "desc": "A deeper frame for reading Tiberius as an FRH case study.",
    },
    {
        "title": "Advanced Character Design Evolution",
        "slug": "advanced-character-design-evolution",
        "source": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Advanced_Character_Design_Evolution_Explainer.v3.docx",
        "section": "Advanced Character Design",
        "desc": "How complex FRH characters evolve from playable concepts into sharper campaign tools.",
    },
    {
        "title": "Joe Bob Gray: Southern Gothic Extreme Example",
        "slug": "joe-bob-gray-southern-gothic-extreme-example",
        "source": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Joe_Bob_Gray_Southern_Gothic_Extreme_Example.md",
        "section": "Advanced Character Design",
        "desc": "An edge-case character example for seeing how far the design language can bend.",
    },
    {
        "title": "Optional Pregenerated Characters Library",
        "slug": "optional-pregenerated-characters-library",
        "source": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "FRH_Optional_Pregenerated_Characters_Library_Index.md",
        "section": "Optional Characters",
        "desc": "A library index for optional ready-to-play and example characters.",
    },
]


CHARACTERS = [
    {
        "title": "Tiberius Sinclair",
        "slug": "tiberius-sinclair",
        "html": SOURCE / "Tiberius Sinclair.htm",
        "pdf": SOURCE / "Tiberius_Sinclair.pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Autafon Deliamber",
        "slug": "autafon-deliamber",
        "html": SOURCE / "Characters" / "Autafon Deliamber.v2.htm",
        "pdf": SOURCE / "Characters" / "Amber_Deliamber.pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Chaney Markov",
        "slug": "chaney-markov",
        "html": SOURCE / "Characters" / "Chaney Markov.v2.htm",
        "pdf": SOURCE / "Characters" / "Chaney_Markov.pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Chuff",
        "slug": "chuff",
        "html": SOURCE / "Characters" / "Chuff.htm",
        "pdf": SOURCE / "Characters" / "Chuff_(Melodys_Ally).pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Crispin Pollick",
        "slug": "crispin-pollick",
        "html": SOURCE / "Characters" / "Crispin Pollick.v2.htm",
        "pdf": SOURCE / "Characters" / "Crispin_Pollick.pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "GURPS 3rd 1923 Supernatural Template",
        "slug": "gurps-3rd-1923-supernatural-template",
        "html": SOURCE / "Characters" / "GURPS_3rd_1923_Supernatural.htm",
        "pdf": SOURCE / "GURPS_3rd_1923_Supernatural.pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Matthew Bridges",
        "slug": "matthew-bridges",
        "html": SOURCE / "Characters" / "Matthew Bridges.v2.htm",
        "pdf": SOURCE / "Characters" / "Matthew_Bridges_(High_Risk_Psychometry).pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Melody Manners",
        "slug": "melody-manners",
        "html": SOURCE / "Characters" / "Melody Manners.htm",
        "pdf": SOURCE / "Characters" / "Melody_Manners.pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Mila Johannson",
        "slug": "mila-johannson",
        "html": SOURCE / "Characters" / "Mila Johannson.htm",
        "pdf": SOURCE / "Characters" / "Mila_Johannson.pdf",
        "group": "Core Character Sheets",
    },
    {
        "title": "Tiberius Sinclair: Insane NPC",
        "slug": "tiberius-sinclair-insane-npc",
        "html": SOURCE / "Advanced_Appendix" / "Tiberius Sinclair - Insane NPC.htm",
        "pdf": SOURCE / "Advanced_Appendix" / "Tiberius_Sinclair_( Insane_NPC).pdf",
        "group": "Advanced Appendix",
    },
    {
        "title": "Autafon Deliamber: Dragon Breath",
        "slug": "autafon-deliamber-dragon-breath",
        "html": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Amber_Deliamber"
        / "Autafon Deliamber (Dragon Breath).htm",
        "pdf": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Amber_Deliamber"
        / "Autafon_Deliamber_(Dragon_Breath).pdf",
        "group": "Advanced Character Design",
    },
    {
        "title": "Autafon Deliamber: Martial Artist",
        "slug": "autafon-deliamber-martial-artist",
        "html": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Amber_Deliamber"
        / "Autafon Deliamber (Martial Artist).htm",
        "pdf": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Amber_Deliamber"
        / "Autafon_Deliamber_(Martial_Artist).pdf",
        "group": "Advanced Character Design",
    },
    {
        "title": "Autafon Deliamber: Psi",
        "slug": "autafon-deliamber-psi",
        "html": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Amber_Deliamber"
        / "Autafon Deliamber (Psi).htm",
        "pdf": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Amber_Deliamber"
        / "Autafon_Deliamber_(Psi).pdf",
        "group": "Advanced Character Design",
    },
    {
        "title": "Joe Bob Gray: Human Form",
        "slug": "joe-bob-gray-human-form",
        "html": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Joe_Bob_Gray"
        / "Joe Bob Gray (Human Form).htm",
        "pdf": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Joe_Bob_Gray"
        / "Joe_Bob_Gray_(Human_Form).pdf",
        "group": "Advanced Character Design",
    },
    {
        "title": "Joe Bob Gray: Werewolf Form",
        "slug": "joe-bob-gray-werewolf-form",
        "html": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Joe_Bob_Gray"
        / "Joe Bob Gray (Werewolf Form).htm",
        "pdf": SOURCE
        / "Advanced_Character_Design_Evolution"
        / "Joe_Bob_Gray"
        / "Joe_Bob_Gray_(Werewolf_Form).pdf",
        "group": "Advanced Character Design",
    },
    {
        "title": "Adrian Draik",
        "slug": "adrian-draik",
        "html": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Adrian Draik 375 Final_GCB.htm",
        "pdf": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Adrian Draik 375 Final_GCB.pdf",
        "group": "Optional Pregenerated Characters",
    },
    {
        "title": "Gabriel Voss",
        "slug": "gabriel-voss",
        "html": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Gabriel Voss 375 Final_GCB.htm",
        "pdf": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Gabriel Voss 375 Final_GCB.pdf",
        "group": "Optional Pregenerated Characters",
    },
    {
        "title": "Siegfried Vane",
        "slug": "siegfried-vane",
        "html": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Siegfried Vane 375 Final_GCB.htm",
        "pdf": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Siegfried Vane 375 Final_GCB.pdf",
        "group": "Optional Pregenerated Characters",
    },
    {
        "title": "Tomas Solis",
        "slug": "tomas-solis",
        "html": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Tomas Solis 375 Final_GCB.htm",
        "pdf": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "01_Ready_To_Play_Pregens"
        / "Library_Feed"
        / "Tomas Solis 375 Final_GCB.pdf",
        "group": "Optional Pregenerated Characters",
    },
    {
        "title": "Suzette Vale",
        "slug": "suzette-vale",
        "html": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "02_Character_Examples"
        / "Library_Feed"
        / "Suzette Vale 375 Final_GCB.htm",
        "pdf": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "02_Character_Examples"
        / "Library_Feed"
        / "Suzette_Vale_(Vampire_Mortician).pdf",
        "group": "Optional Pregenerated Characters",
    },
    {
        "title": "Father Elias Kane",
        "slug": "father-elias-kane",
        "html": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "03_Advanced_And_Exotic_Options"
        / "Father_Elias_Kane"
        / "Father_Elias_Kane.htm",
        "pdf": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "03_Advanced_And_Exotic_Options"
        / "Father_Elias_Kane"
        / "Father_Elias_Kane.pdf",
        "group": "Advanced and Exotic Options",
    },
    {
        "title": "Silas Rourke",
        "slug": "silas-rourke",
        "html": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "03_Advanced_And_Exotic_Options"
        / "Silas_Rourke"
        / "Silas_Rourke.htm",
        "pdf": SOURCE
        / "FRH_Optional_Pregenerated_Characters_Library"
        / "03_Advanced_And_Exotic_Options"
        / "Silas_Rourke"
        / "Silas_Rourke.pdf",
        "group": "Advanced and Exotic Options",
    },
]

PDF_ONLY = []


def ensure_dirs(target: Target) -> None:
    target.root.mkdir(parents=True, exist_ok=True)
    (target.root / "characters").mkdir(parents=True, exist_ok=True)
    (target.root / "pdf").mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    for encoding in ("utf-8", "cp1252", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def pandoc_fragment(path: Path) -> str:
    source_format = "docx" if path.suffix.lower() == ".docx" else "markdown"
    result = subprocess.run(
        ["pandoc", "-f", source_format, "-t", "html5", "--wrap=none", str(path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout


def extract_body(raw_html: str) -> str:
    match = re.search(r"<body[^>]*>(.*?)</body>", raw_html, flags=re.S | re.I)
    if match:
        return match.group(1)
    return raw_html


def clean_release_text(text: str) -> str:
    mojibake = {
        "\u00c3\u00a9": "\u00e9",
        "\u00c2\u00a0": " ",
        "\u00c2\u00be": "3/4",
        "\u00c2\u00bc": "1/4",
        "\u00e2\u20ac\u2122": "\u2019",
        "\u00e2\u20ac\u0153": "\u201c",
        "\u00e2\u20ac\u009d": "\u201d",
        "\u00e2\u20ac\u201c": "\u2013",
        "\u00e2\u20ac\u00a6": "\u2026",
    }
    for bad, good in mojibake.items():
        text = text.replace(bad, good)
    text = text.replace("Final Guidance", "Release Guidance")
    text = text.replace("05_Tiberius_Example_Playthrough_final.docx", "Tiberius Example Play-Through")
    text = text.replace("Tiberius_Case_Study_Framing..docx", "Tiberius Case Study Framing")
    text = text.replace("Tiberius Sinclair - Insane NPC.htm", "Tiberius Sinclair: Insane NPC")
    text = text.replace("Tiberius Sinclair.htm", "Tiberius Sinclair character sheet")
    text = text.replace("Tiberius Sinclair.chr", "Tiberius Sinclair GCB file")
    text = text.replace("Silas Rourke..htm", "Silas Rourke character sheet")
    text = text.replace("Silas Rourke..chr", "Silas Rourke GCB file")
    text = text.replace("Father Elias Kane.htm", "Father Elias Kane character sheet")
    text = text.replace("Father Elias Kane.chr", "Father Elias Kane GCB file")
    text = text.replace("Father Elias Kane", "Father Elias Kane")
    text = text.replace("Father_Elias_Kane", "Father_Elias_Kane")
    text = text.replace("father-elias-kane", "father-elias-kane")
    text = text.replace("vulnerable", "vulnerable")
    text = text.replace("further", "further")
    text = text.replace("The armored items confer similar protection.", "The armored items confer similar protection.")
    text = text.replace("Example Playthrough", "Example Play-Through")
    text = text.replace("example playthrough", "example play-through")
    text = text.replace("play-thru", "play-through")
    text = text.replace("playthrough", "play-through")
    text = re.sub(r"\bthru\b", "through", text, flags=re.I)
    text = re.sub(r"B[r]unth", "Blunth", text)
    text = text.replace('id="-guidance"', 'id="release-guidance"')
    text = text.replace("â€œ", "&ldquo;").replace("â€", "&rdquo;")
    text = text.replace("â€™", "&rsquo;").replace("â€”", "&mdash;")
    text = text.replace("â€“", "&ndash;").replace("â€˜", "&lsquo;")
    text = re.sub(
        r'<a href="[A-Za-z]:\\[^"]*">([^<]+)</a>',
        lambda match: match.group(1),
        text,
    )
    text = re.sub(
        r"\[([^\]]+)\]\([A-Za-z]:\\[^)]*\)",
        lambda match: match.group(1),
        text,
    )
    text = re.sub(
        r"C:\\Users\\seang\\OneDrive\\Documents\\ChatGPT_[^<\s)]+",
        lambda _match: "~\\ChatGPT_FRH",
        text,
    )
    text = re.sub(
        r'<a href="~\\ChatGPT_FRH[^"]*">([^<]+)</a>',
        lambda match: match.group(1),
        text,
    )
    text = re.sub(r"_?beta(?:[_ -]?v?\d+(?:\.\d+)*)?", "", text, flags=re.I)
    text = re.sub(r"_v\d+(?:\.\d+)*", "", text, flags=re.I)
    text = re.sub(r"\bBeta\b", "", text)
    text = re.sub(r"\bv\d+(?:\.\d+)*\b", "", text)
    text = re.sub(r"\bfinal\b", "", text, flags=re.I)
    text = text.replace("Final_GCB", "GCB")
    text = text.replace("_GCB", "")
    text = text.replace("FHR", "FRH")
    text = text.replace("``", "")
    text = text.replace("`", "")
    text = text.replace("`_final`", "release suffixes")
    text = text.replace("like  and", "like working suffixes and")
    text = text.replace('id="-guidance"', 'id="release-guidance"')
    text = re.sub(r"\s{2,}", " ", text)
    return text


def fix_character_images(target: Target, body: str) -> str:
    image_map = {
        "Crispin Pollick..jpg": "Crispin_Pollick_post-Smoke.jpg",
        "Matthew Bridges..jpg": "Matthew_Bridges_Ben_Grinslade.jpg",
    }
    for bad, good in image_map.items():
        body = body.replace(f'src="{bad}"', f'src="{target.char_image_prefix}{good}"')
    return body


def strip_duplicate_title(fragment: str, title: str) -> str:
    title_pattern = re.escape(title)
    return re.sub(
        rf"^\s*<h1\b[^>]*>\s*{title_pattern}\s*</h1>\s*",
        "",
        fragment,
        count=1,
        flags=re.I,
    )


def add_tiberius_scene_nav(fragment: str) -> str:
    scenes = [
        ("scene-setup", "Scene Setup"),
        ("street-surveillance", "Street Surveillance"),
        ("following-tony", "Following Tony"),
        ("reading-tony", "Reading Tony's Mind"),
        ("taking-control", "Taking Control"),
        ("inside-warehouse", "Inside the Warehouse"),
        ("card-room", "The Card Room"),
        ("grappling-guido", "Grappling Guido"),
        ("clearing-room", "Clearing the Room"),
        ("finding-pauly", "Finding Pauly"),
        ("alfred", "Danger Sense and Alfred"),
        ("escape", "Escape"),
        ("what-this-example-demonstrates", "What This Example Demonstrates"),
    ]
    links = "\n".join(
        f'          <a href="#{anchor}">{html.escape(label)}</a>' for anchor, label in scenes
    )
    nav = f"""<nav class="npp-scene-nav" aria-label="Tiberius play-through scenes">
        <h2>Scene Navigation</h2>
        <div>
{links}
        </div>
      </nav>
"""

    fragment = fragment.replace(
        "<p><strong>Scene Setup</strong></p>",
        f'{nav}<h2 id="scene-setup">Scene Setup</h2>',
        1,
    )
    fragment = re.sub(
        r"<p><em><strong>A quick adventure with The Wraith\.</strong></em></p>\s*",
        '<h2 id="street-surveillance">Street Surveillance</h2>\n',
        fragment,
        count=1,
    )
    markers = [
        ("following-tony", "Following Tony", "<strong>GM:</strong> He continues east toward the river."),
        ("reading-tony", "Reading Tony's Mind", "<strong>T:</strong> OK, I use Telereceive"),
        ("taking-control", "Taking Control", "<strong>T:</strong> I think I found the Jackson boy."),
        ("inside-warehouse", "Inside the Warehouse", "<strong>T:</strong> I get out my pistol and I have Tony walk up the stairs"),
        ("card-room", "The Card Room", "<strong>GM:</strong> Alright, Tony opens the door and looks in."),
        ("grappling-guido", "Grappling Guido", "<strong>T:</strong> Great. I drop my pistol in my coat pocket."),
        ("clearing-room", "Clearing the Room", "<strong>T:</strong> Before that happens, since I am already in his mind, I put him to Sleep."),
        ("finding-pauly", "Finding Pauly", "<strong>T:</strong> OK, I quickly check all the gangsters"),
        ("alfred", "Danger Sense and Alfred", "<strong>GM:</strong> The kit gives you a +1 so you made it by 3."),
        ("escape", "Escape", "<strong>T:</strong> OK, I go back and untie the boy."),
    ]
    for anchor, label, marker in markers:
        index = fragment.find(marker)
        if index != -1:
            paragraph_start = fragment.rfind("<p", 0, index)
            if paragraph_start != -1:
                fragment = (
                    fragment[:paragraph_start]
                    + f'<h2 id="{anchor}">{html.escape(label)}</h2>\n'
                    + fragment[paragraph_start:]
                )

    fragment = re.sub(
        r"<p><strong>What This Example Demonstrates\s*<br\s*/>\s*</strong></p>",
        '<h2 id="what-this-example-demonstrates">What This Example Demonstrates</h2>',
        fragment,
        count=1,
    )
    return fragment


def page_shell(target: Target, title: str, part: str, body: str, prev_href: str | None = None, next_href: str | None = None) -> str:
    nav = (
        f'<a href="{html.escape(target.home_href)}">Reader Home</a> | '
        f'<a href="index.html">NPP Home</a> | '
        f'<a href="characters/index.html">Character Sheets</a> | '
        f'<a href="{html.escape(target.reference_href)}">Reference Gallery</a>'
    )
    footer_links = []
    if prev_href:
        footer_links.append(f'<a href="{html.escape(prev_href)}">Previous</a>')
    footer_links.append('<a class="primary" href="index.html">NPP Home</a>')
    if next_href:
        footer_links.append(f'<a href="{html.escape(next_href)}">Next</a>')
    footer_links.append(f'<a href="{html.escape(target.home_href)}">Reader Home</a>')
    footer = "\n        ".join(footer_links)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} - FRH New Player Packet</title>
  <link rel="stylesheet" href="{html.escape(target.css_href)}">
</head>
<body class="legacy-page npp-page">
  <main class="legacy-main npp-main">
    <div class="legacy-header">
      <p class="part">{html.escape(part)}</p>
      <div class="nav legacy-nav"><p>{nav}</p></div>
    </div>
    <article class="legacy-article npp-article">
      <h1>{html.escape(title)}</h1>
{body}
    </article>
    <div class="page-footer">
      <div class="chapter-nav">
        {footer}
      </div>
      <p class="footer-note">Part of the FRH New Player Packet web release candidate.</p>
    </div>
  </main>
</body>
</html>
"""


def character_shell(target: Target, title: str, body: str, pdf_href: str | None) -> str:
    pdf_link = f' | <a href="{html.escape(pdf_href)}">PDF sheet</a>' if pdf_href else ""
    nav = (
        f'<a href="{html.escape(target.char_home_href)}">Reader Home</a> | '
        '<a href="../index.html">NPP Home</a> | '
        '<a href="index.html">Character Sheets</a>'
        f"{pdf_link}"
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} - FRH Character Sheet</title>
  <link rel="stylesheet" href="{html.escape(target.char_css_href)}">
</head>
<body class="legacy-page npp-page">
  <main class="legacy-main npp-main">
    <div class="legacy-header">
      <p class="part">Character Sheet</p>
      <div class="nav legacy-nav"><p>{nav}</p></div>
    </div>
    <article class="legacy-article npp-character-sheet">
{body}
    </article>
    <div class="page-footer">
      <div class="chapter-nav">
        <a href="index.html">Character Sheets</a>
        <a class="primary" href="../index.html">NPP Home</a>
        <a href="{html.escape(target.char_home_href)}">Reader Home</a>
      </div>
    </div>
  </main>
</body>
</html>
"""


def card(title: str, href: str, desc: str) -> str:
    return (
        '<section class="gallery-card">'
        f"<h3>{html.escape(title)}</h3>"
        f"<p>{html.escape(desc)}</p>"
        f'<p><a href="{html.escape(href)}">Open</a></p>'
        "</section>"
    )


def copy_pdf(target: Target, source: Path, slug: str) -> str | None:
    if not source or not source.exists():
        return None
    dest_name = f"{slug}.pdf"
    shutil.copyfile(source, target.root / "pdf" / dest_name)
    return f"../pdf/{dest_name}"


def build_docs(target: Target) -> None:
    html_files = [f"{doc['slug']}.html" for doc in DOCS]
    for index, doc in enumerate(DOCS):
        fragment = pandoc_fragment(doc["source"])
        fragment = clean_release_text(fragment)
        fragment = strip_duplicate_title(fragment, doc["title"])
        if doc["slug"] == "tiberius-example-playthrough":
            fragment = add_tiberius_scene_nav(fragment)
        prev_href = html_files[index - 1] if index > 0 else None
        if doc["slug"] == "character-creation-guide":
            prev_href = target.edgar_letter_href
        next_href = html_files[index + 1] if index < len(html_files) - 1 else None
        page = page_shell(target, doc["title"], doc["section"], fragment, prev_href, next_href)
        (target.root / f"{doc['slug']}.html").write_text(page, encoding="utf-8")


def build_character_pages(target: Target) -> None:
    for entry in CHARACTERS:
        raw = read_text(entry["html"])
        body = clean_release_text(extract_body(raw))
        body = fix_character_images(target, body)
        body = re.sub(r"<p>\s*(<h[1-6]\b)", r"\1", body, flags=re.I)
        body = re.sub(r"<table\b", '<div class="table-scroll"><table', body, flags=re.I)
        body = re.sub(r"</table>", "</table></div>", body, flags=re.I)
        pdf_href = copy_pdf(target, entry["pdf"], entry["slug"]) if entry["pdf"] else None
        page = character_shell(target, entry["title"], body, pdf_href)
        (target.root / "characters" / f"{entry['slug']}.html").write_text(page, encoding="utf-8")

    for entry in PDF_ONLY:
        copy_pdf(target, entry["pdf"], entry["slug"])


def build_character_index(target: Target) -> None:
    groups: dict[str, list[str]] = {}
    for entry in CHARACTERS:
        desc = "GCB HTML character sheet with a clean reader wrapper."
        if entry["pdf"]:
            desc += " Includes a linked PDF sheet."
        groups.setdefault(entry["group"], []).append(card(entry["title"], f"{entry['slug']}.html", desc))
    for entry in PDF_ONLY:
        groups.setdefault(entry["group"], []).append(
            card(entry["title"], f"../pdf/{entry['slug']}.pdf", "PDF-only character reference.")
        )

    sections = []
    for group, cards in groups.items():
        sections.append(f"<h2>{html.escape(group)}</h2>\n<div class=\"gallery\">\n{''.join(cards)}\n</div>")
    body = "\n".join(sections)
    index = character_shell(target, "Character Sheets", body, None)
    (target.root / "characters" / "index.html").write_text(index, encoding="utf-8")


def build_gurps_lite_page(target: Target) -> None:
    body = f"""
      <p>GURPS Lite Third Edition is a free official download from Warehouse 23. The web packet links to the official source instead of republishing the local PDF copy.</p>
      <p><a href="{html.escape(GURPS_LITE_URL)}">Open the official GURPS Lite Third Edition download page</a></p>
"""
    page = page_shell(target, "GURPS Lite Third Edition", "External Reference", body)
    (target.root / "gurps-lite-third-edition.html").write_text(page, encoding="utf-8")


def build_index(target: Target) -> None:
    readme = read_text(SOURCE / "00_READ_ME_FIRST.txt")
    if "How This Campaign Is Run" in readme:
        readme = readme[readme.index("How This Campaign Is Run") :]
    campaign_note = clean_release_text(html.escape(readme).replace("\n", "<br>\n"))
    by_section: dict[str, list[dict[str, str]]] = {}
    for doc in DOCS:
        by_section.setdefault(doc["section"], []).append(doc)
    sections = []
    for section, docs in by_section.items():
        cards = "".join(
            card(
                doc["title"],
                target.edgar_letter_href if doc["slug"] == "edgar-von-haupt-letter" else f"{doc['slug']}.html",
                doc["desc"],
            )
            for doc in docs
        )
        sections.append(f"<h2>{html.escape(section)}</h2>\n<div class=\"gallery\">\n{cards}\n</div>")
    body = f"""
      <p class="deck">A web-first presentation of the FRH onboarding packet, with clean reader navigation, character sheets, optional examples, and supporting references.</p>
      <div class="workflow">
        <h2>Recommended First Read</h2>
        <ol class="workflow-steps">
          <li><a href="{html.escape(target.edgar_letter_href)}">Edgar Von Haupt Letter</a></li>
          <li><a href="character-creation-guide.html">Character Creation Guide</a></li>
          <li><a href="cloudburg-overview.html">Cloudburg Overview</a></li>
          <li><a href="tiberius-example-playthrough.html">Tiberius Example Play-Through</a></li>
          <li><a href="pregenerated-character-mechanics-overview.html">Pregenerated Character Mechanics Overview</a></li>
        </ol>
      </div>
      <div class="secondary-links">
        <h2>Packet Hubs</h2>
        <ul>
          <li><a href="characters/index.html">Character Sheets</a></li>
          <li><a href="gurps-lite-third-edition.html">GURPS Lite Third Edition official download</a></li>
          <li><a href="{html.escape(target.intro_href)}">Original NPP discussion in the reader transcript</a></li>
        </ul>
      </div>
{''.join(sections)}
      <div class="note">
        <h2>Campaign Table Note</h2>
        <p>{campaign_note}</p>
      </div>
"""
    page = page_shell(target, "FRH New Player Packet", "Reference Packet", body)
    (target.root / "index.html").write_text(page, encoding="utf-8")


def build_all() -> None:
    for target in TARGETS:
        ensure_dirs(target)
        build_docs(target)
        build_character_pages(target)
        build_character_index(target)
        build_gurps_lite_page(target)
        build_index(target)


if __name__ == "__main__":
    build_all()
