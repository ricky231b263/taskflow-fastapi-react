from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import router as auth_router
from tasks import router as tasks_router
from database import Base, engine
import models

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def root():
    return {
        "message": "Task Manager API is running 🚀"
    }