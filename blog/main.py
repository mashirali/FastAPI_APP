from fastapi import FastAPI, Depends, status, Response, HTTPException
from .database import engine, get_db
from .schemas import Blog
from . import models
from sqlalchemy.orm import Session
import schemas


from blog.routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

get_db = get_db

app.include_router(blog.router)
app.include_router(user.router)
