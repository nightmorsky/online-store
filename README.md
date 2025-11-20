"# Online Store

REST API for an online store built with FastAPI and PostgreSQL.

## Tech Stack

- **Framework**: FastAPI 0.119.0
- **Database**: PostgreSQL (asyncpg + psycopg2-binary)
- **ORM**: SQLAlchemy 2.0.41
- **Migrations**: Alembic 1.16.5
- **Validation**: Pydantic 2.11.7
- **Server**: Uvicorn 0.37.0

## Project Structure

```
online-store/
├── app/
│   ├── main.py              # FastAPI application
│   ├── db/
│   │   ├── base.py          # SQLAlchemy Base model
│   │   └── database.py      # Database configuration
│   ├── models/              # SQLAlchemy models
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── category.py
│   │   ├── order.py
│   │   ├── order_item.py
│   │   └── cart_item.py
│   └── schemas/             # Pydantic schemas
├── migrations/              # Alembic migrations
│   └── versions/
├── .env                     # Environment variables
├── alembic.ini             # Alembic configuration
├── pyproject.toml          # Poetry configuration
└── requirements.txt        # Python dependencies

```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/nightmorsky/online-store.git
cd online-store
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
DB_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/online_store
ASYNC_DB_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/online_store
```

### 5. Create the database

```bash
# Connect to PostgreSQL and create the database
psql -U postgres
CREATE DATABASE online_store;
\q
```

### 6. Run migrations

```bash
alembic upgrade head
```

### 7. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be available at: http://localhost:8000

API Documentation (Swagger): http://localhost:8000/docs

Alternative Documentation (ReDoc): http://localhost:8000/redoc

## Working with Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback a migration

```bash
alembic downgrade -1
```

### Check current version

```bash
alembic current
```

## Development

### Adding a new model

1. Create a model in `app/models/`
2. Add the model import to `app/db/base.py`
3. Create a migration: `alembic revision --autogenerate -m "Add new model"`
4. Apply the migration: `alembic upgrade head`

### Code formatting

```bash
black app/
isort app/
```

### Type checking

```bash
mypy app/
```

### Run tests

```bash
pytest
```

## Data Models

- **User** - System users
- **Product** - Products
- **Category** - Product categories
- **Order** - Orders
- **OrderItem** - Order items
- **CartItem** - Shopping cart items

## License

MIT
" 
