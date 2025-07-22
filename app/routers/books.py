from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from .. import schemas
from ..crud import BookCRUD
from ..database import Database

class BookRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/books", tags=["Books"])
        self.crud = BookCRUD()
        self.db = Database()
        self._add_routes()

    async def get_db(self):
        async with self.db.get_session() as session:
            yield session

    def _add_routes(self):
        @self.router.post("/", response_model=schemas.Book)
        async def create(book: schemas.BookCreate, db: AsyncSession = Depends(self.get_db)):
            return await self.crud.create_book(db, book)

        @self.router.get("/", response_model=list[schemas.Book])
        async def read_all(db: AsyncSession = Depends(self.get_db)):
            return await self.crud.get_books(db)

        @self.router.get("/{book_id}", response_model=schemas.Book)
        async def read(book_id: UUID, db: AsyncSession = Depends(self.get_db)):
            book = await self.crud.get_book(db, book_id)
            if book is None:
                raise HTTPException(status_code=404, detail="Book not found")
            return book

        @self.router.delete("/{book_id}")
        async def delete(book_id: UUID, db: AsyncSession = Depends(self.get_db)):
            success = await self.crud.delete_book(db, book_id)
            if not success:
                raise HTTPException(status_code=404, detail="Book not found")
            return {"message": "Book deleted"}

    def get_router(self):
        return self.router
