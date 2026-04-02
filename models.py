
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class BookRequest:
    title: str
    author: str
    is_apa: bool

@dataclass
class Listing:
    seller: str
    title: str
    author: str
    edition_text: Optional[str]
    pub_year: Optional[int]
    condition: Optional[str]
    item_price: Decimal
    shipping_price: Decimal
    total_price: Decimal
    url: str

@dataclass
class ErrorRecord:
    book_title: str
    book_author: str
    seller: str
    error: str
