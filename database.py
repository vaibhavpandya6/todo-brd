from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

# Create database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///todo.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the engine
Base.metadata.create_all(engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()