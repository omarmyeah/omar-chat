import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
CSRF_TOKEN_LENGTH = os.getenv("CSRF_TOKEN_LENGTH")
COOKIE_ID_LENGTH = os.getenv("COOKIE_ID_LENGTH")