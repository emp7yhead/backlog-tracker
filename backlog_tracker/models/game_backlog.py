from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from backlog_tracker.db.session import Base
from backlog_tracker.models.abstract_backlog import AbstractBacklog

game_tags_reference_table = Table(
    'game_tags_reference_table',
    Base.metadata,
    Column('game_id', Integer, ForeignKey('backlog_game.id')),
    Column('tags.id', Integer, ForeignKey('tags.id')),
)


class BacklogGame(AbstractBacklog):
    __tablename__ = 'backlog_game'

    tags = relationship('tags', secondary=game_tags_reference_table)
