from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint
#This handles the user sending data to us
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True #defaults to true if not provided

class PostCreate(PostBase):
    pass


# data user gets back on account creation
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
            from_attributes=True

# Reponse to User
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        from_attributes=True
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes=True

# data user sends
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
     email: EmailStr
     password: str


class Token(BaseModel):
     access_token: str
     token_type: str

class TokenData(BaseModel):
     id: Optional[str] = None


class Vote(BaseModel):
     post_id: int
     dir: int