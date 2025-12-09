from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine, Base
from app.routers import users

# Create DB tables (won't alter existing tables)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
def ensure_db_columns():
	"""Ensure missing columns exist. This runs a safe ALTER TABLE that
	adds the `password` column if the table was created earlier without it.
	"""
	with engine.begin() as conn:
		conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS password VARCHAR;"))


app.include_router(users.router)
