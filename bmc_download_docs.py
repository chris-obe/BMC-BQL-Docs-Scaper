
#!/usr/bin/env python3
"""
Download a curated subset of the BMC Helix Discovery Query Language docs and
merge the main text into a single Markdown file. Handy when you want to give a
chatbot (or a tired brain) the same reference material you keep Googling.

Usage:
    python bmc_download_docs.py output.md
If no output filename is provided, defaults to "bmc_query_language_docs.md".

Dependencies:
    pip install requests beautifulsoup4 tqdm
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# List of documentation URLs that cover the bulk of the BQL reference.
URLS = [
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Key-expressions/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Query-Language-Functions/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Logical-and-arithmetic-expressions/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Name-binding/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Traversals/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/NODECOUNT-Expressions/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Search-Flags-and-limits/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Ordering/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/The-SHOW-Clause/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Explode/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/Results-after-processing/",
    "https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Helix-Discovery/DAAS/Using/Using-the-Search-and-Reporting-service/Using-the-Query-Language/A-Note-on-Performance/",
]

# Strip headers/footers/toc that just add noise when feeding the docs into a model.
EXCLUDE_SELECTORS = [
    "nav",
    "header",
    "footer",
    ".xnavigation",
    ".breadcrumb",
    ".tree",
    ".panel",
    ".footnotes",
    ".comments",
    ".toc",
    ".copyright",
    ".banner",
    ".header",
    ".footer",
    ".table-of-content",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; DocumentationScraper/1.0; +https://openai.com)"
}

# Explicit list keeps the extraction predictable across docs.
CONTENT_TAGS = ("h1", "h2", "h3", "h4", "p", "pre", "code", "li")

DEFAULT_OUTPUT = Path("bmc_query_language_docs.md")


def extract_main_content(html: str) -> str:
    """Peel away the chrome and keep the useful text/code samples."""
    soup = BeautifulSoup(html, "html.parser")

    for selector in EXCLUDE_SELECTORS:
        for elem in soup.select(selector):
            elem.decompose()

    text_parts: list[str] = []
    for elem in soup.find_all(CONTENT_TAGS):
        # Skip inline code snippets that are already emitted by the wrapping <pre>.
        if elem.name == "code" and elem.parent and elem.parent.name == "pre":
            continue

        text = elem.get_text(" ", strip=True)
        if not text:
            continue

        if elem.name.startswith("h"):
            level = int(elem.name[1])
            text_parts.append(f"{'#' * level} {text}")
        elif elem.name in {"pre", "code"}:
            text_parts.append(f"\n```\n{text}\n```")
        else:
            text_parts.append(text)

    return "\n\n".join(text_parts).strip()


def fetch_and_merge(urls: Iterable[str], destination: Path) -> None:
    """Download each page and append the cleaned content into destination."""
    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open("w", encoding="utf-8") as f_out, requests.Session() as session:
        for url in tqdm(urls, desc="Downloading pages"):
            try:
                response = session.get(url, headers=HEADERS, timeout=30)
                response.raise_for_status()
            except requests.RequestException as exc:
                print(f"Failed to fetch {url}: {exc}", file=sys.stderr)
                continue

            content = extract_main_content(response.text)
            f_out.write(f"\n\n---\n\n# Source: {url}\n\n{content}\n")


def main() -> None:
    output_arg = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    fetch_and_merge(URLS, output_arg)
    print(f"\nDone! Combined documentation saved to {output_arg}")


if __name__ == "__main__":
    main()
