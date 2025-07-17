from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Use SQLite for now; you can change this to PostgreSQL later
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./smartbiz.db")

# Create DB engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
