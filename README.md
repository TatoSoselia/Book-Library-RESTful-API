# Book-Library-RESTful-API

A simple RESTful API for managing a book library, built with FastAPI, async SQLAlchemy, and PostgreSQL.

## Quick Start

### 1. Clone & Setup
```bash
git clone <repo-url>
cd Book-Library-RESTful-API
```

Create a `.env` file in the root:
```
# PostgreSQL DB Config
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres

# SQLAlchemy/AsyncPG DB URL
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres
```

### 2. Run with Docker (Recommended)
```bash
docker-compose up --build
```
Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.
