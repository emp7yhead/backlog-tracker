"""add_password

Revision ID: 8756aba26493
Revises: 7e2f8af5d0c7
Create Date: 2023-01-29 23:08:46.634148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8756aba26493'
down_revision = '7e2f8af5d0c7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
