import os

from dotenv import find_dotenv, load_dotenv

# since .env isn't in src/
load_dotenv(find_dotenv())

# use pooled for the application but direct for the migrations
# use os.environ because wanna raise an error if not found since app basically won't work without the db
DATABASE_URL = os.environ["DATABASE_URL_POOLED"]

# number of bytes in our urlsafe generated csrf token and session id
CSRF_TOKEN_BYTES = 32
COOKIE_ID_BYTES = 32

ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]