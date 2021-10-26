"""followers

Revision ID: 651ff10bb71d
Revises: 42b6e0daf9ee
Create Date: 2021-10-25 20:59:11.024227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651ff10bb71d'
down_revision = '42b6e0daf9ee'
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
