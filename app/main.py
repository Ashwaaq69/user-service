from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine, Base
from app.routers import users

# Create DB tables 
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
def ensure_db_columns():
	with engine.begin() as conn:
		conn.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS password VARCHAR;"))


app.include_router(users.router)
