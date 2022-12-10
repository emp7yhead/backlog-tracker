from sqlalchemy import Column, Integer, String
from backlog_tracker.db.session import Base


class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)

    def __repr__(self):
        return f"<tag({self.title})>"
