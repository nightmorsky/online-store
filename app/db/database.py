import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import text
from app.config import settings


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)

async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False)


# Dependency for FastAPI routes
async def get_db():
    async with async_session() as session:
        yield session


# Test connection (for debugging)
if __name__ == "__main__":
    import asyncio
    
    async def test_connection():
        print(f"Connecting to: {settings.DATABASE_URL_asyncpg}")
        async with async_engine.connect() as conn:
            result = await conn.execute(text("SELECT VERSION()"))
            version = result.scalar()
            print(f"✓ Database connected successfully!")
            print(f"PostgreSQL version: {version}")
    
    asyncio.run(test_connection()) 