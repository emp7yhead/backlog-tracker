from typing import ClassVar
from sqlalchemy import Column, Integer, String, Time

from backlog_tracker.db.session import Base


class AbstractBacklog(Base):
    __abstract__: ClassVar[bool] = True

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String())
    required_time = Column(Time)
