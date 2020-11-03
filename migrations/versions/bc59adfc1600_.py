"""empty message

Revision ID: bc59adfc1600
Revises: 5710ae58a987
Create Date: 2020-10-28 19:52:56.408213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc59adfc1600'
down_revision = '5710ae58a987'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('url', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('document', 'url')
    # ### end Alembic commands ###
