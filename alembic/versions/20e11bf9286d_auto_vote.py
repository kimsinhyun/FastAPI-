"""auto-vote

Revision ID: 20e11bf9286d
Revises: 8d4381f37c63
Create Date: 2022-08-01 13:01:02.967326

"""
from pdb import post_mortem
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20e11bf9286d'
down_revision = '8d4381f37c63'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['post_id'], ['posts.id'], ondelete="CASCADE"),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('votes')
    pass
