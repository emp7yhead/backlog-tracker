"""add_tags_and_game

Revision ID: 8ec94514d842
Revises: a116a1a3ad5c
Create Date: 2022-12-11 04:21:29.572043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec94514d842'
down_revision = 'a116a1a3ad5c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_tags_reference_table', sa.Column('tags_id', sa.Integer(), nullable=True))
    op.drop_constraint('game_tags_reference_table_tags.id_fkey', 'game_tags_reference_table', type_='foreignkey')
    op.create_foreign_key(None, 'game_tags_reference_table', 'tags', ['tags_id'], ['id'])
    op.drop_column('game_tags_reference_table', 'tags.id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_tags_reference_table', sa.Column('tags.id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'game_tags_reference_table', type_='foreignkey')
    op.create_foreign_key('game_tags_reference_table_tags.id_fkey', 'game_tags_reference_table', 'tags', ['tags.id'], ['id'])
    op.drop_column('game_tags_reference_table', 'tags_id')
    # ### end Alembic commands ###
