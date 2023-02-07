from typing import ClassVar
from sqlalchemy import Column, Integer, String, Time

from src.database import Base


class AbstractBacklog(Base):
    __abstract__: ClassVar[bool] = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String())
    description = Column(String())
    required_time = Column(Time)
