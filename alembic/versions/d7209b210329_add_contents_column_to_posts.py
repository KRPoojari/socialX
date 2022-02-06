"""add contents column to posts

Revision ID: d7209b210329
Revises: d69e693031cb
Create Date: 2022-02-05 14:59:06.063418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7209b210329'
down_revision = 'd69e693031cb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
    pass
