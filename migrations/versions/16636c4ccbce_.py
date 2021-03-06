"""empty message

Revision ID: 16636c4ccbce
Revises: c99da400bde4
Create Date: 2018-10-19 11:38:38.926188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16636c4ccbce'
down_revision = 'c99da400bde4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shop_cart', sa.Column('subTotal', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shop_cart', 'subTotal')
    # ### end Alembic commands ###
