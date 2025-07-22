from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import Base, Database
from .routers.books import BookRouter


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = Database()
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

book_router = BookRouter()
app.include_router(book_router.get_router())
