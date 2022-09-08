from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(blog_id: int, blog: schemas.Blog, db: Session):
    myblog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not myblog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} is not available')
    myblog.update(blog.dict())
    db.commit()
    return 'updated'

def show_id(blog_id: int, db: Session):
    get_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {blog_id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {blog_id} is not available'}

    return get_blog
