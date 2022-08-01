"""create post table

Revision ID: 9282dd2042d5
Revises: 
Create Date: 2022-08-01 11:57:27.913347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9282dd2042d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
