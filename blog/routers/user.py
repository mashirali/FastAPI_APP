from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
from blog import schemas
from blog import database
from blog import models
from blog import hashing
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{user_id}", response_model=schemas.ShowUser)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.get_user_id(user_id, db)
