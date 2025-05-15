from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from api.settings import Settings

engine = create_async_engine(Settings().DATABASE_URL)

Base = declarative_base()

async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
