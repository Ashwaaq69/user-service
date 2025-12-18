from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserCreate(UserBase):
    password: str  # Plain password from request

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    password: Optional[str] = None  # Optional password update

class User(UserBase):
    id: int
    hashed_password: str  # Hashed password in response
class UserOut(UserBase):
    id: int    
    class Config:
        orm_mode = True