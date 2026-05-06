import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
APP_ENV = os.getenv("APP_ENV", "development")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data():
    return {
        "environment": APP_ENV,
        "message": "Hello from FastAPI running in Kubernetes!",
        "items": [
            {"id": 1, "name": "Pod"},
            {"id": 2, "name": "Service"},
            {"id": 3, "name": "Deployment"},
        ],
    }

@app.get("/health")
def health():
    return {"status": "ok"}