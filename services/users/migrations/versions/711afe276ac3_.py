"""empty message

Revision ID: 711afe276ac3
Revises: 3b51820d1eb0
Create Date: 2018-03-15 15:20:37.360378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711afe276ac3'
down_revision = '3b51820d1eb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###