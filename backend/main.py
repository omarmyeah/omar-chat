from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Crucial CORS configuration for different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-react-frontend.com"],  # replace with real react origin
    allow_credentials=True,                            # Required for cookies
    allow_methods=["*"],
    allow_headers=["X-CSRF-Token", "Content-Type", "Authorization"], # Allow custom header back
)

app.add_api_route()