import pymupdf


async def read_pdf(file_path: str) -> list[dict]:
    try:
        pages = []
        with pymupdf.open(file_path) as document:
            for page_number, page in enumerate(document):
                text = page.get_text("text", sort=True).strip()
                if not text:
                    continue
                pages.append({"page_number": page_number + 1,"text": text,})

        return pages

    except Exception as e:
        raise RuntimeError(f"Error reading PDF file: {e}") 