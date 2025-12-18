from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


# VALIDATION
# USER
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


# RESPONSE MODEL
class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# VOTE
class Vote(BaseModel):
    post_id: int
    dir: int


# POST
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True


# PAKE JOIN
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True


# # PAKE JOIN
# class PostOne(BaseModel):
#     title: str
#     email: str

#     class Config:
#         from_attributes = True


# JWT Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
