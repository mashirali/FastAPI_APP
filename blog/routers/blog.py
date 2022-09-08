from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
from blog import schemas
from blog import database
from blog import models
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    return blog.destroy(blog_id, db)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog_by_id(blog_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(blog_id, request, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get('/{blog_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    return blog.show_id(blog_id, db)
