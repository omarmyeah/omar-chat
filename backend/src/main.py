from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from .auth import auth_routers
from .core.config import ALLOWED_ORIGINS, DATABASE_URL
from .messaging import messaging_routers, messaging_websockets


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
        pool_pre_ping=True,  # great for serverless DBs like Neon when connections go idle
    )

    session_factory = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False, 
    )

    # store in state for access
    app.state.db_session_factory = session_factory

    yield 

    # cleanly close pooled conns
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

# Crucial CORS configuration for different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS, 
    allow_credentials=True, # Required for cookies
    allow_methods=["*"],
    allow_headers=["X-CSRF-Token", "Content-Type", "Authorization"], # Allow custom header back
)

# include routers.
app.include_router(auth_routers.router)
app.include_router(messaging_routers.router)
app.include_router(messaging_websockets.router)