import os

from dotenv import load_dotenv, find_dotenv

# since .env isn't in src/
load_dotenv(find_dotenv())

# use pooled for the application but direct for the migrations
DATABASE_URL = os.getenv("DATABASE_URL_POOLED")
CSRF_TOKEN_BYTES = 32
COOKIE_ID_BYTES = 32

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]