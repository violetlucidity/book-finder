
from pathlib import Path
from models import BookRequest


def parse_input_file(filepath: Path):
    regular, apa = [], []
    in_apa = False
    for line in filepath.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        if line.lower() == '[apa]':
            in_apa = True
            continue
        if ' - ' not in line:
            continue
        title, author = line.split(' - ', 1)
        book = BookRequest(title.strip(), author.strip(), in_apa)
        (apa if in_apa else regular).append(book)
    return regular, apa
