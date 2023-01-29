from sqlalchemy import Column, Integer, String, UniqueConstraint
from backlog_tracker.db.session import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint('username', 'email'),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=20))
    email = Column(String(length=20))
    password = Column(String(length=128))

    def __repr__(self):
        return f"<User({self.name})>"
