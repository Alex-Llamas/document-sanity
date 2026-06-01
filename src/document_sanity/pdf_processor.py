import fitz
from pathlib import Path
from typing import Optional

def extract_pdf_page_as_png(pdf_path: Path, output_path: Path, page_num: int = 0) -> bool:
    """Extract a specific page from a PDF and save it as a PNG image."""
    try:
        doc = fitz.open(pdf_path)
        if page_num >= len(doc):
            return False

        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x zoom for better quality
        pix.save(output_path)
        doc.close()
        return True
    except Exception as e:
        print(f"Error extracting PDF page {page_num}: {e}")
        return False

def extract_pdf_page_text(pdf_path: Path, page_num: int = 1) -> Optional[str]:
    """Extract text from a specific page of a PDF."""
    try:
        doc = fitz.open(pdf_path)
        if page_num >= len(doc):
            return None

        page = doc.load_page(page_num)
        text = page.get_text().strip()
        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF page {page_num}: {e}")
        return ""

def escape_latex_text(text: str) -> str:
    """Escape special LaTeX characters in plain text."""
    s = text
    s = s.replace('\\', '\\textbackslash{}')
    s = s.replace('&', '\\&')
    s = s.replace('%', '\\%')
    s = s.replace('$', '\\$')
    s = s.replace('#', '\\#')
    s = s.replace('_', '\\_')
    s = s.replace('{', '\\{')
    s = s.replace('}', '\\}')
    s = s.replace('~', '\\textasciitilde{}')
    s = s.replace('^', '\\textasciicircum{}')
    return s
