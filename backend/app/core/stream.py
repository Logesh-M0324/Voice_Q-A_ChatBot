from typing import Generator
import time

def stream_chunks(text: str) -> Generator[str, None, None]:
    words = text.split()
    chunk = []

    for w in words:
        chunk.append(w)
        if len(chunk) >= 8:
            yield " ".join(chunk)
            chunk = []
            time.sleep(0.05)

    if chunk:
        yield " ".join(chunk)
