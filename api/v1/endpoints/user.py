from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
import crud

router = APIRouter()

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/")
def add_user(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name, email)

