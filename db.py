from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import setting

engine = create_engine(setting.DATABASE_URL, echo=True, future=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Generates a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
