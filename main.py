from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from app.database.database import Base, engine
from app.models import organization
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth
import os
allowed_origins_raw = os.getenv("ALLOWED_ORIGINS", "")
allowed_origins = [origin.strip() for origin in allowed_origins_raw.split(",") if origin.strip()]

app = FastAPI()
Base.metadata.create_all(bind=engine)

#허용할 프론트엔드 주소 
origins = [
    "http://localhost:3000",  # Next.js 개발 서버
]

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 또는 ["*"]로 전체 허용
    allow_credentials=True,
    allow_methods=["*"],              # POST, GET, OPTIONS 등
    allow_headers=["*"],
)

app.include_router(auth.router)