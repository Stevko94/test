from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.posts.db import database
from app.posts import models
from app.posts.schemas import PostRead, UserRead

router = APIRouter()


# GET /api/posts?status=draft&include=tags,user
@router.get("/", response_model=List[PostRead])
def read_posts(status: str, include: str, db: Session = Depends(database.SessionLocal)):
    posts = db.query(models.Post).filter(models.Post.status == status).all()

    if "tags" in include:
        for post in posts:
            post.tags = [tag.name for tag in post.tags]
    if "user" in include:
        for post in posts:
            post.user = post.user.name

    return posts


# GET /api/posts/1?include=tags,user,comments
@router.get("/{post_id}", response_model=PostRead)
def read_post(post_id: int, include: str, db: Session = Depends(database.SessionLocal)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if "tags" in include:
        post.tags = [tag.name for tag in post.tags]
    if "user" in include:
        post.user = post.user.name
    if "comments" in include:
        post.comments = [comment.content for comment in post.comments]

    return post


# GET /api/users/1?include=posts,comments
@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, include: str, db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if "posts" in include:
        user.posts = [post.title for post in user.posts]
    if "comments" in include:
        user.comments = [comment.content for comment in user.comments]

    return user
