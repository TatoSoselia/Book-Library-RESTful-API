import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"

Base = declarative_base()

class Database:
    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL, echo=True)
        self.SessionLocal = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        async with self.SessionLocal() as session:
            yield session
