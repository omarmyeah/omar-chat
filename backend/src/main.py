from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth import auth_routers
from .messaging import messaging_routers, messaging_websockets
from .config import ALLOWED_ORIGINS

app = FastAPI()

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