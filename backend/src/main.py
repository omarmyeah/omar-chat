from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth import auth_routers
from .messaging import messaging_websockets
from .messaging import messaging_routers

app = FastAPI()

# Crucial CORS configuration for different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-react-frontend.com"],  # replace with real react origin
    allow_credentials=True,                            # Required for cookies
    allow_methods=["*"],
    allow_headers=["X-CSRF-Token", "Content-Type", "Authorization"], # Allow custom header back
)

# include routers.
app.include_router(auth_routers.router)
app.include_router(messaging_routers.router)
# idk about this one, since live_messaging is websockets so idk if a router needed.
app.include_router(messaging_websockets.router)