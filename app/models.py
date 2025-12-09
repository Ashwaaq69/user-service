from sqlalchemy import column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = column(Integer, primary_key=True, index=True)
    name = column(String, index=True)
    email = column(String, unique=True, index=True)
    age = column(Integer, nullable = False)
    