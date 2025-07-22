from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String, nullable=True)
