from fastapi import FastAPI, WebSocket,WebSocketDisconnect
from app import model
from app.config import settings
from app.database import Base, engine
from app.routes.base import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(api_router)


@app.get("/")
def home():
    return {"message": "Student Management API is running"}


@app.get("/is_working")
def health():
    return {"status": "ok"}

