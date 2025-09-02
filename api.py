from fastapi import FastAPI
from utils import (
    check_quote,
    add_quote,
    get_quote,
    get_random_quote,
    get_top_quotes,
    update_quote,
)
from models import Quote, SortOptions
from typing import List

app = FastAPI()


@app.get("/")
async def root() -> str:
    return "Hello World"


@app.post("/add")
async def add(quote: str, source: str, weight: int) -> str:
    if check_quote(quote, source):
        id = add_quote(quote, source, weight)
        return id
    return ""


@app.get("/get_random", response_model=Quote)
async def get_random() -> Quote:
    return get_random_quote()


@app.get("/get_top", response_model=List[Quote])
async def get_top(count: int, options: SortOptions) -> List[Quote]:
    return get_top_quotes(count, options)


@app.put("/view_quote/{quote_id}")
# TODO: think about security
async def view_quote(quote_id: str) -> bool:
    new_quote = get_quote(quote_id)
    new_quote.views += 1
    return update_quote(quote_id, new_quote)


@app.put("/like_quote/{quote_id}")
# TODO: think about security
async def like_quote(quote_id: str) -> bool:
    new_quote = get_quote(quote_id)
    new_quote.likes += 1
    return update_quote(quote_id, new_quote)


@app.put("/dislike_quote/{quote_id}")
# TODO: think about security
async def dislike_quote(quote_id: str) -> bool:
    new_quote = get_quote(quote_id)
    new_quote.dislikes += 1
    return update_quote(quote_id, new_quote)
