
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from services import user_service
from db import get_db

router = APIRouter()  # <-- This is needed!


# Dependency injection in FastAPI endpoints
@router.post("/users/")
def api_create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service.create_user(db, user)
    return {"message": "User created successfully"}
