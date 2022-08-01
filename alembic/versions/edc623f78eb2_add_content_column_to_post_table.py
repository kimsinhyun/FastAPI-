"""add content column to post table

Revision ID: edc623f78eb2
Revises: 9282dd2042d5
Create Date: 2022-08-01 12:19:43.333942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edc623f78eb2'
down_revision = '9282dd2042d5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
