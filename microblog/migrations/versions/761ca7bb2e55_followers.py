"""followers

Revision ID: 761ca7bb2e55
Revises: 8daa5d1f4d4c
Create Date: 2018-09-30 10:51:44.799253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '761ca7bb2e55'
down_revision = '8daa5d1f4d4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
