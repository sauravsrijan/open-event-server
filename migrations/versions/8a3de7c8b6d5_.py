"""empty message

Revision ID: 8a3de7c8b6d5
Revises: 55fd4c6ae8b2
Create Date: 2018-08-06 23:44:16.489323

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8a3de7c8b6d5'
down_revision = '55fd4c6ae8b2'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sessions', 'ends_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('sessions', 'starts_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sessions', 'starts_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    op.alter_column('sessions', 'ends_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
    # ### end Alembic commands ###