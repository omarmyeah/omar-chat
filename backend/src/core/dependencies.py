# get session / engine
import os
from .config import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,  # great for serverless DBs like Neon when connections go idle
)

async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,  # prevents surprise lazy-load errors after commit
)

async def get_session():
    async with async_session_factory() as session:
        yield session