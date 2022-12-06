from sqlalchemy import Column, Integer, String
from backlog_tracker.db.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<User({self.name})>"
