from sqlalchemy import select
from sqlalchemy.ext import IntegrityError
from sqlalchemy.orm import Session
from app import models, schemas


#create user

def create_user(db: Session, user: schemas.UserCreate):
    user = models.User(**user_in.dict()), 
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise ValueError("User with this email already exists")
    return user  

#get users

def get_users(db: Session, skip: int = 0, limit: int = 100):
    stmt = select(models.User).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()  

#get user by id
def get_user(db: Session, user_id: int):
    return db.get(models.User, user_id)


#get user by email
def get_user_by_email(db: Session, email: str):
    stmt = select(models.User).where(models.User.email == email)
    return db.execute(stmt).scalars().first()


#update user
def update_user(db: Session, user_id: int, user_in: schemas.UserUpdate):
    user = db.get(models.User, user_id)
    if not user:
        return None
    data = user_in.dict(exclude_unset=True)
    for k, v in data.items():
        setattr(user, k, v)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


#delete user
def delete_user(db: Session, user_id: int):
    user = db.get(models.User, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user