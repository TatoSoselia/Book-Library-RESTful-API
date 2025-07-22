from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

class BookCRUD:
    async def create_book(self, db: AsyncSession, book: schemas.BookCreate):
        db_book = models.Book(**book.model_dump())
        db.add(db_book)
        await db.commit()
        await db.refresh(db_book)
        return db_book

    async def get_books(self, db: AsyncSession):
        result = await db.execute(select(models.Book))
        return result.scalars().all()

    async def get_book(self, db: AsyncSession, book_id: int):
        result = await db.execute(select(models.Book).where(models.Book.id == book_id))
        return result.scalar_one_or_none()

    async def delete_book(self, db: AsyncSession, book_id: int):
        book = await self.get_book(db, book_id)
        if book:
            await db.delete(book)
            await db.commit()
        return book
