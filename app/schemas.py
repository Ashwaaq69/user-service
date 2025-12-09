from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

class User(UserBase):
    id: int

class UserOut(User):
    
    class Config:
        orm_mode = True  # <-- For Pydantic v1
        # from_attributes = True  # <-- Use this only if you are using Pydantic v2
