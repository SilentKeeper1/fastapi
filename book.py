from fastapi import FastAPI, Path, Query
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books_db: List[Book] = [
    Book(id=1, title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", year=1979),
    Book(id=2, title="1984", author="George Orwell", year=1949),
    Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
    Book(id=4, title="Dune", author="Frank Herbert", year=1965),
    Book(id=5, title="The Lord of the Rings", author="J.R.R. Tolkien", year=1954),
]



@app.get("/books", response_model=List[Book])
def get_all_books():
    return books_db


@app.get("/books/{book_id}", response_model=Optional[Book])
def get_book_by_id(book_id: int = Path(..., description="ID книжки для пошуку")):
    for book in books_db:
        if book.id == book_id:
            return book
    return None