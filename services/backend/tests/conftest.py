from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backlog_tracker.db.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base.metadata.create_all(bind=engine)


def db_session():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
