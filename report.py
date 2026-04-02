
from pathlib import Path
from datetime import datetime
from decimal import Decimal
from typing import Dict, List
from models import Listing, ErrorRecord
from config import config


def generate_report(all_listings: Dict[str, List[Listing]], errors: List[ErrorRecord], regular_books, apa_books) -> Path:
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    out = config.OUTPUT_DIR / f'book_price_report_{ts}.txt'
    out.parent.mkdir(exist_ok=True)
    with out.open('w', encoding='utf-8') as f:
        f.write('BOOK PRICE COMPARISON REPORT
')
        f.write(f'Shipping estimate (when unknown): ${config.SHIPPING_ESTIMATE}

')
        for seller, lst in all_listings.items():
            f.write(f'--- {seller} ---
')
            subtotal = Decimal('0')
            for l in lst:
                f.write(f'{l.title} - {l.author}
')
                f.write(f'  Price: ${l.item_price:.2f} + ${l.shipping_price:.2f} = ${l.total_price:.2f}
')
                f.write(f'  Link: {l.url}
')
                subtotal += l.total_price
            f.write(f'TOTAL ({seller}): ${subtotal:.2f}

')
        if errors:
            f.write('ERRORS:
')
            for e in errors:
                f.write(f'- {e.book_title} - {e.book_author} | {e.seller}: {e.error}
')
    return out
