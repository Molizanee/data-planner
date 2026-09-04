"""Renderiza docs/planner.html em docs/planner.pdf via Chromium headless."""

from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

DOCS_DIR = Path(__file__).resolve().parents[2] / "docs"
HTML_PATH = DOCS_DIR / "planner.html"
PDF_PATH = HTML_PATH.with_suffix(".pdf")

PAGE_FORMAT = "A4"
MARGIN = {"top": "12mm", "right": "12mm", "bottom": "12mm", "left": "12mm"}


def render(html_path: Path, pdf_path: Path) -> None:
    """Converte um arquivo HTML local em PDF preservando o layout de impressao."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            page = browser.new_page()
            page.goto(html_path.as_uri(), wait_until="networkidle")
            page.emulate_media(media="print")
            page.evaluate("async () => { await document.fonts.ready; }")
            page.pdf(
                path=pdf_path,
                format=PAGE_FORMAT,
                margin=MARGIN,
                print_background=True,
                prefer_css_page_size=True,
            )
        finally:
            browser.close()


def main() -> int:
    if not HTML_PATH.is_file():
        print(f"arquivo nao encontrado: {HTML_PATH}", file=sys.stderr)
        return 1
    try:
        render(HTML_PATH, PDF_PATH)
    except PlaywrightError as exc:
        print(f"falha ao renderizar {HTML_PATH.name}: {exc}", file=sys.stderr)
        if "Executable doesn't exist" in str(exc):
            print("execute: uv run playwright install chromium", file=sys.stderr)
        return 1
    print(PDF_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
