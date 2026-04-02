
import argparse
from pathlib import Path
from config import config
from input_parser import parse_input_file
from selection import process_books
from report import generate_report


def main():
    p = argparse.ArgumentParser(description='Book price comparison tool')
    p.add_argument('input_file')
    p.add_argument('--shipping', type=float, default=config.SHIPPING_ESTIMATE)
    p.add_argument('--delay', type=float, default=config.REQUEST_DELAY)
    args = p.parse_args()

    config.SHIPPING_ESTIMATE = args.shipping
    config.REQUEST_DELAY = args.delay

    regular, apa = parse_input_file(Path(args.input_file))
    listings, errors = process_books(regular, apa)
    report_path = generate_report(listings, errors, regular, apa)
    print('Report written to', report_path)


if __name__ == '__main__':
    main()
