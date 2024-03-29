"""rename_user_to_username

Revision ID: c74770a59a17
Revises: 8756aba26493
Create Date: 2023-01-29 23:50:19.385593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c74770a59a17'
down_revision = '8756aba26493'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=20), nullable=True))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
