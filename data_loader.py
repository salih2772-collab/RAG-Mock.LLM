from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader


def load_txt(file_path: Path) -> Dict:
    text = file_path.read_text(encoding="utf-8")
    return {
        "content": text,
        "source": file_path.name,
        "type": "txt"
    }


def load_pdf(file_path: Path) -> Dict:
    reader = PdfReader(str(file_path))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n".join(pages)
    return {
        "content": text,
        "source": file_path.name,
        "type": "pdf"
    }


def load_documents(data_dir: str) -> List[Dict]:
    documents = []
    path = Path(data_dir)

    for file in path.iterdir():
        if file.suffix.lower() == ".txt":
            documents.append(load_txt(file))
        elif file.suffix.lower() == ".pdf":
            documents.append(load_pdf(file))

    return documents
