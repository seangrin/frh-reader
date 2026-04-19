from __future__ import annotations

import csv
import html
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "FRH_GMA_Portable_Review_Package"


@dataclass(frozen=True)
class SiteTarget:
    name: str
    root: Path
    output: Path
    home_href_from_output: str
    css_base: Path


TARGETS = [
    SiteTarget(
        name="flat",
        root=ROOT / "thread_clean_reader_site",
        output=ROOT / "thread_clean_reader_site" / "gma_review",
        home_href_from_output="../index.html",
        css_base=ROOT / "thread_clean_reader_site" / "thread_style.css",
    ),
    SiteTarget(
        name="structured",
        root=ROOT / "FRH_HTML_Reader",
        output=ROOT / "FRH_HTML_Reader" / "content" / "gma_review",
        home_href_from_output="../../index.html",
        css_base=ROOT / "FRH_HTML_Reader" / "assets" / "css" / "thread_style.css",
    ),
]


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CODE_RE = re.compile(r"`([^`]+)`")
STRONG_RE = re.compile(r"\*\*([^*]+)\*\*")
EM_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
TRANSCRIPT_RE = re.compile(r"^\[(S\d{2}-\d{2}-\d{3})\]\s+\[([^\]]+)\]\s+([^:]+):\s?(.*)$")


def sanitize_windows_paths(text: str) -> str:
    """Redact machine-specific Windows path roots while preserving useful provenance."""

    def repl(match: re.Match[str]) -> str:
        path = match.group(0).replace("/", "\\")
        path = re.sub(r"^[A-Za-z]:\\(?=[A-Za-z]:\\)", "", path)
        path = re.sub(r"^[Cc]:\\Users\\seang\\OneDrive\\Documents\\", "", path)
        path = re.sub(r"^[A-Za-z]:\\", "", path)
        return "~\\" + path

    return re.sub(r"(?<![A-Za-z])[A-Za-z]:[/\\][^`\"'<>†\r\n]+", repl, text)


def portable_relative_href(from_file: Path, to_file: Path) -> str:
    import os

    return os.path.relpath(to_file, from_file.parent).replace("\\", "/")


def title_from_path(path: Path) -> str:
    stem = path.stem
    if stem == "README":
        return "README"
    return stem.replace("_", " ").replace("-", " ")


def html_page(
    title: str,
    body: str,
    out_file: Path,
    target: SiteTarget,
    part: str = "GMA Transcript Corpus",
    page_links: list[tuple[str, Path]] | None = None,
) -> str:
    css_href = portable_relative_href(out_file, target.css_base)
    index_href = portable_relative_href(out_file, target.output / "index.html")
    transcript_href = portable_relative_href(out_file, target.output / "transcript_index.html")
    home_href = portable_relative_href(out_file, target.root / "index.html")
    utility_links = [
        ("Reader Home", home_href),
        ("GMA Transcript Index", transcript_href),
        ("GMA Package Home", index_href),
    ]
    utility_html = " | ".join(f'<a href="{html.escape(href)}">{html.escape(label)}</a>' for label, href in utility_links)
    page_nav = ""
    if page_links:
        page_nav_items = []
        for label, link_path in page_links:
            page_nav_items.append(
                f'<a href="{html.escape(portable_relative_href(out_file, link_path))}">{html.escape(label)}</a>'
            )
        page_nav = f'\n    <div class="chapter-nav gma-local-nav">{"".join(page_nav_items)}</div>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} - FRH GMA Review Corpus</title>
  <link rel="stylesheet" href="{html.escape(css_href)}">
</head>
<body class="gma-page">
  <main class="gma-main">
    <p class="part">{html.escape(part)}</p>
    <div class="nav gma-nav">
      <p>{utility_html}</p>{page_nav}
    </div>
    {body}
    <div class="page-footer gma-footer">
      <div class="nav gma-nav">
        <p>{utility_html}</p>{page_nav}
      </div>
    </div>
  </main>
</body>
</html>
"""


def convert_inline(text: str, current_source: Path, current_output: Path, target: SiteTarget) -> str:
    text = sanitize_windows_paths(text)
    escaped = html.escape(text)

    def link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        href = html.unescape(match.group(2))
        if href.startswith(("http://", "https://", "mailto:", "#")):
            final_href = href
        else:
            base = current_source.parent
            raw_target = (base / href).resolve()
            if raw_target.suffix.lower() in {".md", ".txt", ".tsv"} and raw_target.exists():
                rel_src = raw_target.relative_to(SOURCE)
                final_target = target.output / rel_src.with_suffix(".html")
                final_href = portable_relative_href(current_output, final_target)
            else:
                final_href = href
        return f'<a href="{html.escape(final_href)}">{html.escape(label)}</a>'

    escaped = MD_LINK_RE.sub(link_repl, escaped)
    escaped = CODE_RE.sub(lambda m: f"<code>{m.group(1)}</code>", escaped)
    escaped = STRONG_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", escaped)
    escaped = EM_RE.sub(lambda m: f"<em>{m.group(1)}</em>", escaped)
    return escaped


def parse_front_matter(lines: list[str]) -> tuple[list[str], list[str]]:
    if not lines or lines[0].strip() != "---":
        return [], lines
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[1:idx], lines[idx + 1 :]
    return [], lines


def front_matter_html(lines: list[str]) -> str:
    if not lines:
        return ""
    rows = []
    key = None
    values: list[str] = []
    for raw in lines + [""]:
        line = raw.rstrip("\n")
        if re.match(r"^[A-Za-z0-9_]+:\s*", line):
            if key is not None:
                rows.append((key, "<br>".join(html.escape(v) for v in values if v)))
            key, value = line.split(":", 1)
            values = [value.strip().strip('"')]
        elif line.strip().startswith("- ") and key is not None:
            values.append(line.strip()[2:].strip().strip('"'))
        elif line.strip() and key is not None:
            values.append(line.strip().strip('"'))
    if not rows:
        return ""
    body = "\n".join(f"<tr><th>{html.escape(k)}</th><td>{v}</td></tr>" for k, v in rows)
    return f'<details class="metadata"><summary>Source metadata</summary><table>{body}</table></details>'


def flush_list(out: list[str], list_type: str | None) -> None:
    if list_type:
        out.append(f"</{list_type}>")


def render_transcript_line(
    line_id: str,
    timestamp: str,
    speaker: str,
    words: str,
    source_file: Path,
    out_file: Path,
    target: SiteTarget,
) -> str:
    return (
        '<p class="transcript-line">'
        f'<span class="line-id">{html.escape(line_id)}</span> '
        f'<span class="timestamp">{html.escape(timestamp)}</span> '
        f'<strong>{html.escape(speaker)}</strong>: {convert_inline(words, source_file, out_file, target)}'
        "</p>"
    )


def markdown_to_html(text: str, source_file: Path, out_file: Path, target: SiteTarget) -> tuple[str, str]:
    text = sanitize_windows_paths(text)
    try:
        pandoc_input = preprocess_markdown_for_pandoc(text)
        result = subprocess.run(
            [
                "pandoc",
                "--from",
                "markdown+yaml_metadata_block+pipe_tables-smart",
                "--to",
                "html",
                "--wrap",
                "none",
            ],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            input=pandoc_input,
        )
        body = rewrite_pandoc_links(result.stdout, source_file, out_file, target)
        title_match = re.search(r"<h1[^>]*>(.*?)</h1>", body, flags=re.S)
        title = title_from_path(source_file)
        if title_match:
            title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip() or title
        return title, body
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    lines = text.splitlines()
    fm, body_lines = parse_front_matter(lines)
    out: list[str] = []
    title = title_from_path(source_file)
    metadata = front_matter_html(fm)
    if metadata:
        out.append(metadata)

    in_code = False
    code_lines: list[str] = []
    list_type: str | None = None
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if not para:
            return
        text_line = " ".join(para).strip()
        para = []
        transcript = TRANSCRIPT_RE.match(text_line)
        if transcript:
            out.append(render_transcript_line(*transcript.groups(), source_file, out_file, target))
        else:
            out.append(f"<p>{convert_inline(text_line, source_file, out_file, target)}</p>")

    for raw in body_lines:
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                flush_para()
                flush_list(out, list_type)
                list_type = None
                in_code = True
            continue
        if in_code:
            code_lines.append(raw)
            continue
        if not line.strip():
            flush_para()
            flush_list(out, list_type)
            list_type = None
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_para()
            flush_list(out, list_type)
            list_type = None
            level = min(len(heading.group(1)), 4)
            heading_text = heading.group(2).strip()
            if level == 1 and title == title_from_path(source_file):
                title = re.sub(r"<[^>]+>", "", heading_text)
            out.append(f"<h{level}>{convert_inline(heading_text, source_file, out_file, target)}</h{level}>")
            continue
        bullet = re.match(r"^[-*]\s+(.+)$", line)
        numbered = re.match(r"^\d+\.\s+(.+)$", line)
        if bullet or numbered:
            flush_para()
            next_type = "ul" if bullet else "ol"
            if list_type != next_type:
                flush_list(out, list_type)
                out.append(f"<{next_type}>")
                list_type = next_type
            item = (bullet or numbered).group(1)
            out.append(f"<li>{convert_inline(item, source_file, out_file, target)}</li>")
            continue
        if line.startswith("> "):
            flush_para()
            flush_list(out, list_type)
            list_type = None
            out.append(f"<blockquote>{convert_inline(line[2:], source_file, out_file, target)}</blockquote>")
            continue
        transcript = TRANSCRIPT_RE.match(line)
        if transcript:
            flush_para()
            flush_list(out, list_type)
            list_type = None
            out.append(render_transcript_line(*transcript.groups(), source_file, out_file, target))
            continue
        para.append(line)

    flush_para()
    flush_list(out, list_type)
    if in_code:
        out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return title, "\n".join(out)


def preprocess_markdown_for_pandoc(text: str) -> str:
    out: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        is_transcript = TRANSCRIPT_RE.match(line) is not None
        is_scene = line.startswith("### Scene:")
        if is_transcript or is_scene:
            if out and out[-1] != "":
                out.append("")
            out.append(line)
            out.append("")
        else:
            out.append(raw)
    return "\n".join(out) + "\n"


def rewrite_pandoc_links(body: str, source_file: Path, out_file: Path, target: SiteTarget) -> str:
    def href_repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        href = html.unescape(match.group(2))
        if href.startswith(("http://", "https://", "mailto:", "#")):
            final_href = href
        else:
            link_path, hash_mark, fragment = href.partition("#")
            raw_target = (source_file.parent / link_path).resolve()
            if raw_target.suffix.lower() in {".md", ".txt", ".tsv"} and raw_target.exists():
                rel_src = raw_target.relative_to(SOURCE)
                final_target = target.output / rel_src.with_suffix(".html")
                final_href = portable_relative_href(out_file, final_target)
                if hash_mark:
                    final_href += f"#{fragment}"
            else:
                final_href = href
        return f'href={quote}{html.escape(final_href)}{quote}'

    body = re.sub(r'href=(["\'])([^"\']+)\1', href_repl, body)

    def transcript_repl(match: re.Match[str]) -> str:
        line_id, timestamp, speaker, words = match.groups()
        return (
            '<p class="transcript-line">'
            f'<span class="line-id">{line_id}</span> '
            f'<span class="timestamp">{timestamp}</span> '
            f'<strong>{speaker}</strong>: {words}</p>'
        )

    return re.sub(
        r"<p>\[(S\d{2}-\d{2}-\d{3})\]\s+\[([^\]]+)\]\s+([^:<]+):\s?(.*?)</p>",
        transcript_repl,
        body,
        flags=re.S,
    )


def tsv_to_html(source_file: Path) -> tuple[str, str]:
    title = title_from_path(source_file)
    with source_file.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    if not rows:
        return title, "<p>No rows found.</p>"
    headers, data = rows[0], rows[1:]
    head = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    body_rows = []
    for row in data:
        cells = []
        for idx, cell in enumerate(row):
            cell = sanitize_windows_paths(cell)
            cell_text = html.escape(cell)
            header = headers[idx] if idx < len(headers) else ""
            if header in {"segment_md", "review_md"} and cell:
                html_href = cell.replace("\\", "/")
                html_href = re.sub(r"\.(md|txt|tsv)$", ".html", html_href)
                cell_text = f'<a href="{html.escape(html_href)}">{html.escape(cell)}</a>'
            cells.append(f"<td>{cell_text}</td>")
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    table = f'<div class="table-wrap"><table class="data-table"><thead><tr>{head}</tr></thead><tbody>{"".join(body_rows)}</tbody></table></div>'
    return title, f"<h1>{html.escape(title)}</h1>\n{table}"


def source_to_output(source_file: Path, target: SiteTarget) -> Path:
    rel = source_file.relative_to(SOURCE)
    return target.output / rel.with_suffix(".html")


def sessions_root() -> Path:
    return SOURCE / "GMA_Gold_Star_Corpus" / "sessions"


def session_dirs() -> list[Path]:
    return sorted(p for p in sessions_root().iterdir() if p.is_dir())


def session_output_dir(session_dir: Path, target: SiteTarget) -> Path:
    return target.output / session_dir.relative_to(SOURCE)


def session_index_output(session_dir: Path, target: SiteTarget) -> Path:
    return session_output_dir(session_dir, target) / "index.html"


def session_label(session_dir: Path) -> str:
    name = session_dir.name
    m = re.match(r"Session_(\d{2})_(\d{4}-\d{2}-\d{2})(?:_(.*))?$", name)
    if not m:
        return name.replace("_", " ")
    suffix = f" - {m.group(3).replace('_', ' ')}" if m.group(3) else ""
    return f"Session {int(m.group(1))}: {m.group(2)}{suffix}"


def read_manifest(session_dir: Path) -> list[dict[str, str]]:
    manifest = session_dir / "segment_manifest.tsv"
    if not manifest.exists():
        return []
    with manifest.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def read_session_metadata(session_dir: Path) -> dict[str, str]:
    session_wide = session_dir / "session_wide.md"
    if not session_wide.exists():
        return {}
    lines, _ = parse_front_matter(session_wide.read_text(encoding="utf-8-sig").splitlines())
    meta: dict[str, str] = {}
    for line in lines:
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            meta[key.strip()] = sanitize_windows_paths(value.strip().strip('"'))
    return meta


def build_source_nav(target: SiteTarget) -> dict[Path, list[tuple[str, Path]]]:
    nav: dict[Path, list[tuple[str, Path]]] = {}
    dirs = session_dirs()
    for idx, session_dir in enumerate(dirs):
        current_session_index = session_index_output(session_dir, target)
        prev_session = session_index_output(dirs[idx - 1], target) if idx > 0 else None
        next_session = session_index_output(dirs[idx + 1], target) if idx + 1 < len(dirs) else None

        session_links: list[tuple[str, Path]] = [("Session Index", current_session_index)]
        if prev_session:
            session_links.append(("Previous Session", prev_session))
        if next_session:
            session_links.append(("Next Session", next_session))

        for source_name in ["session_wide.md", "segment_manifest.tsv", "npc_overlay_report.tsv"]:
            source = session_dir / source_name
            if source.exists():
                nav[source.resolve()] = session_links

        rows = read_manifest(session_dir)
        for row_idx, row in enumerate(rows):
            segment_source = (session_dir / row["segment_md"]).resolve()
            review_source = (session_dir / row["review_md"]).resolve()
            prev_segment = session_dir / rows[row_idx - 1]["segment_md"] if row_idx > 0 else None
            next_segment = session_dir / rows[row_idx + 1]["segment_md"] if row_idx + 1 < len(rows) else None
            segment_links: list[tuple[str, Path]] = [("Session Index", current_session_index)]
            if prev_segment:
                segment_links.append(("Previous Segment", source_to_output(prev_segment, target)))
            if next_segment:
                segment_links.append(("Next Segment", source_to_output(next_segment, target)))
            segment_links.append(("Review Notes", source_to_output(session_dir / row["review_md"], target)))
            nav[segment_source] = segment_links

            review_links: list[tuple[str, Path]] = [("Session Index", current_session_index)]
            review_links.append(("Transcript Segment", source_to_output(session_dir / row["segment_md"], target)))
            if prev_segment:
                review_links.append(("Previous Segment", source_to_output(prev_segment, target)))
            if next_segment:
                review_links.append(("Next Segment", source_to_output(next_segment, target)))
            nav[review_source] = review_links
    return nav


def session_summary_html(session_dir: Path) -> str:
    meta = read_session_metadata(session_dir)
    rows = read_manifest(session_dir)
    summary_bits = []
    if meta.get("session_title"):
        summary_bits.append(f'<strong>Title:</strong> {html.escape(meta["session_title"])}')
    if meta.get("real_date_played"):
        summary_bits.append(f'<strong>Played:</strong> {html.escape(meta["real_date_played"])}')
    if meta.get("in_game_date"):
        summary_bits.append(f'<strong>In-world:</strong> {html.escape(meta["in_game_date"])}')
    count = len(rows)
    summary_bits.append(f'<strong>Curated segments:</strong> {count}')
    scenes = []
    for row in rows:
        scene_text = row.get("scene_titles", "")
        if scene_text:
            scenes.extend(scene_text.split(" | "))
    unique_scenes = []
    for scene in scenes:
        if scene and scene not in unique_scenes:
            unique_scenes.append(scene)
    scene_html = ""
    if unique_scenes:
        scene_items = "".join(f"<li>{html.escape(scene)}</li>" for scene in unique_scenes[:12])
        scene_html = f"<h3>Scene Summary</h3><ul>{scene_items}</ul>"
    return f'<div class="hero gma-summary"><p>{"<br>".join(summary_bits)}</p>{scene_html}</div>'


def build_transcript_master_index(target: SiteTarget) -> None:
    out_file = target.output / "transcript_index.html"
    cards = []
    for session_dir in session_dirs():
        rows = read_manifest(session_dir)
        session_index = session_index_output(session_dir, target)
        session_wide = session_output_dir(session_dir, target) / "session_wide.html"
        meta = read_session_metadata(session_dir)
        subtitle = []
        if meta.get("session_title"):
            subtitle.append(meta["session_title"])
        if meta.get("real_date_played"):
            subtitle.append(meta["real_date_played"])
        if meta.get("in_game_date"):
            subtitle.append(meta["in_game_date"])
        first_scenes = []
        for row in rows[:2]:
            if row.get("scene_titles"):
                first_scenes.extend(row["scene_titles"].split(" | "))
        preview = "; ".join(first_scenes[:4])
        links = [
            f'<a href="{html.escape(portable_relative_href(out_file, session_index))}">Open session index</a>',
            f'<a href="{html.escape(portable_relative_href(out_file, session_wide))}">Session wide context</a>',
        ]
        cards.append(
            '<section class="session-block">'
            f"<h2>{html.escape(session_label(session_dir))}</h2>"
            f'<p class="mini">{html.escape(" | ".join(subtitle))}</p>'
            f'<p>{html.escape(preview)}</p>'
            f'<p class="link-row">{" ".join(links)}</p>'
            "</section>"
        )
    body = (
        "<h1>GMA Transcript Master Index</h1>"
        '<p class="deck">The top-level index for the converted GMA transcript corpus. Open a session index to see its summary, curated segments, review notes, manifest, and NPC overlay report.</p>'
        + "\n".join(cards)
    )
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html_page("GMA Transcript Master Index", body, out_file, target), encoding="utf-8")


def build_per_session_indexes(target: SiteTarget) -> None:
    dirs = session_dirs()
    for idx, session_dir in enumerate(dirs):
        out_file = session_index_output(session_dir, target)
        session_wide = session_output_dir(session_dir, target) / "session_wide.html"
        manifest_html = session_output_dir(session_dir, target) / "segment_manifest.html"
        npc_html = session_output_dir(session_dir, target) / "npc_overlay_report.html"
        rows = read_manifest(session_dir)
        segment_items = []
        for row_idx, row in enumerate(rows):
            segment_md = session_dir / row["segment_md"]
            review_md = session_dir / row["review_md"]
            segment_html = source_to_output(segment_md, target)
            review_html = source_to_output(review_md, target)
            scenes = row.get("scene_titles", "").replace(" | ", "; ")
            label = f'{row.get("segment_index", "")}. {row.get("segment_id", "")} ({row.get("start", "")} to {row.get("end", "")})'
            next_text = "Start here" if row_idx == 0 else "Open segment"
            segment_items.append(
                "<li>"
                f'<a href="{html.escape(portable_relative_href(out_file, segment_html))}">{html.escape(label)}</a>'
                f' <span class="muted">|</span> <a href="{html.escape(portable_relative_href(out_file, review_html))}">review notes</a>'
                f' <span class="muted">|</span> <span class="mini">{html.escape(next_text)}</span>'
                f'<br><span class="mini">{html.escape(scenes)}</span>'
                "</li>"
            )
        page_links: list[tuple[str, Path]] = []
        if idx > 0:
            page_links.append(("Previous Session", session_index_output(dirs[idx - 1], target)))
        if rows:
            page_links.append(("First Segment", source_to_output(session_dir / rows[0]["segment_md"], target)))
        if idx + 1 < len(dirs):
            page_links.append(("Next Session", session_index_output(dirs[idx + 1], target)))
        body = (
            f"<h1>{html.escape(session_label(session_dir))}</h1>"
            f"{session_summary_html(session_dir)}"
            '<div class="link-row gma-support-links">'
            f'<a href="{html.escape(portable_relative_href(out_file, session_wide))}">Session wide context</a>'
            f'<a href="{html.escape(portable_relative_href(out_file, manifest_html))}">Manifest table</a>'
            f'<a href="{html.escape(portable_relative_href(out_file, npc_html))}">NPC overlay report</a>'
            "</div>"
            "<h2>Curated Segments</h2>"
            f'<ol class="segment-list">{"".join(segment_items)}</ol>'
        )
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(html_page(session_label(session_dir), body, out_file, target, page_links=page_links), encoding="utf-8")


def build_session_index_alias(target: SiteTarget) -> None:
    out_file = target.output / "session_index.html"
    transcript = target.output / "transcript_index.html"
    body = (
        "<h1>GMA Transcript Master Index</h1>"
        '<p class="deck">This compatibility page points to the GMA Transcript Master Index.</p>'
        f'<p><a href="{html.escape(portable_relative_href(out_file, transcript))}">Open the GMA Transcript Master Index</a></p>'
    )
    out_file.write_text(html_page("GMA Transcript Master Index", body, out_file, target), encoding="utf-8")


def build_package_home(target: SiteTarget, top_docs: list[Path]) -> None:
    out_file = target.output / "index.html"
    doc_items = []
    for source_doc in top_docs:
        html_doc = source_to_output(source_doc, target)
        doc_items.append(f'<li><a href="{html.escape(portable_relative_href(out_file, html_doc))}">{html.escape(source_doc.name)}</a></li>')
    corpus_readme = target.output / "GMA_Gold_Star_Corpus" / "README.html"
    body = f"""
<h1>FRH GMA Portable Review Package</h1>
<p class="deck">HTML conversion of the portable review corpus, preserving the package documents, session-wide context, curated transcript segments, review notes, manifests, and NPC overlay reports.</p>
<div class="workflow">
  <h2>Start Here</h2>
  <ol class="workflow-steps">
    <li><a href="GMA_ONBOARDING.html">GMA Onboarding</a></li>
    <li><a href="SESSION_PRIORITY.html">Session Priority</a></li>
    <li><a href="READING_PROTOCOL.html">Reading Protocol</a></li>
    <li><a href="NPC_OVERLAY_GUIDE.html">NPC Overlay Guide</a></li>
    <li><a href="transcript_index.html">GMA Transcript Master Index</a></li>
  </ol>
</div>
<div class="secondary-links">
  <h2>Package Documents</h2>
  <ul>{''.join(doc_items)}</ul>
</div>
<div class="secondary-links">
  <h2>Corpus</h2>
  <ul>
    <li><a href="{html.escape(portable_relative_href(out_file, corpus_readme))}">Gold Star Corpus README</a></li>
    <li><a href="transcript_index.html">Browse transcript sessions</a></li>
  </ul>
</div>
"""
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(html_page("FRH GMA Portable Review Package", body, out_file, target), encoding="utf-8")


def convert_all(target: SiteTarget) -> None:
    if target.output.exists():
        shutil.rmtree(target.output)
    target.output.mkdir(parents=True, exist_ok=True)
    top_docs = []
    nav_by_source = build_source_nav(target)
    for source_file in sorted(SOURCE.rglob("*")):
        if not source_file.is_file():
            continue
        if source_file.suffix.lower() not in {".md", ".txt", ".tsv"}:
            continue
        out_file = source_to_output(source_file, target)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        if source_file.parent == SOURCE and source_file.suffix.lower() == ".md":
            top_docs.append(source_file)
        if source_file.suffix.lower() == ".tsv":
            title, body = tsv_to_html(source_file)
        else:
            text = source_file.read_text(encoding="utf-8-sig")
            title, body = markdown_to_html(text, source_file, out_file, target)
            if not body.lstrip().startswith("<h1"):
                body = f"<h1>{html.escape(title)}</h1>\n{body}"
        out_file.write_text(
            html_page(title, body, out_file, target, page_links=nav_by_source.get(source_file.resolve())),
            encoding="utf-8",
        )
    build_transcript_master_index(target)
    build_per_session_indexes(target)
    build_session_index_alias(target)
    build_package_home(target, sorted(top_docs))


def main() -> None:
    for target in TARGETS:
        convert_all(target)


if __name__ == "__main__":
    main()
