"""Adding verified column to users table

Revision ID: a125bd683e1c
Revises: 34a455dd3fc9
Create Date: 2020-03-05 00:24:33.176191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a125bd683e1c'
down_revision = '34a455dd3fc9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('verified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'verified')
    # ### end Alembic commands ###
