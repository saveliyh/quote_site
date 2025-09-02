from typing import List
from models import Quote, SortOptions


def check_quote(quote: str, source: str) -> bool:
    # TODO: impolement logic
    return True


def add_quote(quote: str, source: str, weight: int) -> str:
    # TODO: implement logic
    return "quote_id:123"


def get_random_quote() -> Quote:
    # TODO: implement logic
    return Quote(quote="quote", source="source", id="quote_id:123", views=10)


def get_top_quotes(count: int, options: SortOptions) -> List[Quote]:
    # TODO: implement logic
    return []


def get_quote(quote_id: str) -> Quote:
    # TODO: implement logic
    return Quote(quote="quote", source="source", id="quote_id:123", views=10)


def update_quote(quote_id: str, quote: Quote) -> bool:
    # TODO: implement logic
    return True
