from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None

class Book(BookCreate):
    id: UUID
