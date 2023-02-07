from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from src.database import Base
from src.models import AbstractBacklog

game_tags_reference_table = Table(
    'game_tags_reference_table',
    Base.metadata,
    Column('game_id', Integer, ForeignKey('backlog_game.id')),
    Column('tags_id', Integer, ForeignKey('tags.id')),
)


class BacklogGame(AbstractBacklog):
    __tablename__ = 'backlog_game'

    tags = relationship('Tags', secondary=game_tags_reference_table)
