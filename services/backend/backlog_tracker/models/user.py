from sqlalchemy import Column, Integer, String
from backlog_tracker.db.session import Base

MAX_STRING_LENGTH = 20


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=MAX_STRING_LENGTH))
    email = Column(String(length=MAX_STRING_LENGTH))
    password = Column(String(length=MAX_STRING_LENGTH))

    def __repr__(self):
        return f"<User({self.name})>"
