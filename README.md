# user-service
Mini User Management System 🚀
A lightweight, FastAPI-based user management system with full CRUD operations, authentication, and PostgreSQL/SQLite database support.

✨ Features
✅ User CRUD Operations (Create, Read, Update, Delete)

✅ Secure Password Hashing with bcrypt

✅ Email Uniqueness Validation

✅ RESTful API Design

✅ SQLAlchemy ORM for database operations

✅ Pydantic Data Validation

✅ Database Migrations support

✅ Error Handling with proper HTTP status codes

🛠 Tech Stack
FastAPI - Modern web framework

SQLAlchemy - Database ORM

PostgreSQL/SQLite - Database

bcrypt - Password hashing

Pydantic - Data validation

Uvicorn - ASGI server

🚀 Quick Start
Prerequisites
Python 3.8+

PostgreSQL (optional) or SQLite

pip package manager

Installation
Clone and navigate to project

bash
git clone <repository-url>
cd Mini-User-Management
Create virtual environment

bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Or install manually:

bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary bcrypt passlib
Database Setup

Option A: PostgreSQL

bash
# Create PostgreSQL database
createdb users_db

Option B: SQLite (No setup needed)

Configure Database Connection
Edit app/database.py:

python
# For PostgreSQL:
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/users_db"

# For SQLite:
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
Run the Application

bash
uvicorn app.main:app --reload