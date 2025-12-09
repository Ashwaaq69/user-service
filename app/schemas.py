from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name : str = Field(..., min_length=1, max_length=128)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)
    

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)   
    
    
class UserUpdate(BaseModel):
    name : str = Field(None, min_length=1, max_length=128)
    email: EmailStr |None = None
    age: int |None = Field(None, ge=0, le=120)
    
    
    
    class UserOut(UserBase):
        id: int

        class Config:
            orm_mode = True
   