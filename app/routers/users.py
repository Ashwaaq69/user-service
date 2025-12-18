from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# ✅ POST /users/ - Create user
@router.post("/users/", response_model=schemas.User, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# ✅ GET /users/ - List all users 
@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# ✅ GET /users/{user_id} - Get specific user
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ✅ PUT /users/{user_id} - Update user
@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if email is being changed and already exists
    if user.email and user.email != db_user.email:
        existing = crud.get_user_by_email(db, email=user.email)
        if existing:
            raise HTTPException(status_code=409, detail="Email already registered")
    
    return crud.update_user(db=db, user_id=user_id, user_in=user)

# ✅ DELETE /users/{user_id} - Delete user
@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db=db, user_id=user_id)
    return None