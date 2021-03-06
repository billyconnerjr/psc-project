"""removed remember

Revision ID: 7712e434f7bc
Revises: a125bd683e1c
Create Date: 2020-03-05 04:17:29.775844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7712e434f7bc'
down_revision = 'a125bd683e1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'remember')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('remember', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###
