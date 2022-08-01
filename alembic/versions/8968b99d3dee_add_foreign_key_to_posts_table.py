"""add foreign-key to posts table

Revision ID: 8968b99d3dee
Revises: cad3da642de8
Create Date: 2022-08-01 12:32:58.049455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8968b99d3dee'
down_revision = 'cad3da642de8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_users_fk',
        source_table="posts",
        referent_table="users",
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete="CASCADE"
    )
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
