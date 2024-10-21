from pydantic import BaseModel
from typing import List

# Base schema for posts
class PostBase(BaseModel):
    title: str
    status: str

# Schema for reading posts
class PostRead(PostBase):
    id: int
    user_id: int
    tags: List[str] = []
    comments: List[str] = []

    class Config:
        orm_mode = True

# Schema for reading tags
class TagRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Schema for reading comments
class CommentRead(BaseModel):
    id: int
    content: str
    user_id: int

    class Config:
        orm_mode = True

# Base schema for users
class UserBase(BaseModel):
    name: str

# Schema for reading users
class UserRead(UserBase):
    id: int
    posts: List[str] = []
    comments: List[str] = []

    class Config:
        orm_mode = True