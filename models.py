from pydantic import BaseModel


class Quote(BaseModel):
    quote: str
    source: str
    id: str
    views: int | None = None
    likes: int | None = None
    dislikes: int | None = None
    weight: int | None = None


class SortOptions(BaseModel):
    sort_by: str = "likes"
    decending_order: bool = True
