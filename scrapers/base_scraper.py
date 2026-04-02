from abc import ABC, abstractmethod
from decimal import Decimal
import time, requests
from bs4 import BeautifulSoup
from models import BookRequest, Listing
from config import config

class BaseScraper(ABC):
    def __init__(self, name: str):
        self.name = name
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": config.USER_AGENT})

    def _delay(self):
        time.sleep(config.REQUEST_DELAY)

    def _parse_price(self, text: str) -> Decimal:
        import re
        m = re.search(r"\$([\d,]+\.\d+|[\d,]+)", text)
        return Decimal(m.group(1).replace(',', '')) if m else Decimal('0')

    @abstractmethod
    def search_and_pick(self, book: BookRequest):
        ...
