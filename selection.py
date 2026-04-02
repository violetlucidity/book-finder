
from typing import Dict, List, Tuple
from models import BookRequest, Listing, ErrorRecord
from scrapers import AmazonScraper, EbayScraper, AbebooksScraper, BookshopScraper, AppiScraper


def process_books(regular_books, apa_books) -> Tuple[Dict[str, List[Listing]], List[ErrorRecord]]:
    scrapers = {
        'Amazon': AmazonScraper(),
        'eBay': EbayScraper(),
        'AbeBooks': AbebooksScraper(),
        'Bookshop.org': BookshopScraper(),
    }
    listings: Dict[str, List[Listing]] = {}
    errors: List[ErrorRecord] = []

    for book in regular_books + apa_books:
        for seller, scraper in scrapers.items():
            try:
                listing = scraper.search_and_pick(book)
                if listing:
                    listings.setdefault(seller, []).append(listing)
            except Exception as e:
                errors.append(ErrorRecord(book.title, book.author, seller, str(e)))
        if book.is_apa:
            try:
                appi = AppiScraper()
                listing = appi.search_and_pick(book)
                if listing:
                    listings.setdefault('APPI.org', []).append(listing)
            except Exception as e:
                errors.append(ErrorRecord(book.title, book.author, 'APPI.org', str(e)))

    return listings, errors
