"""empty message

Revision ID: 74774f234d12
Revises: 625511d483c2
Create Date: 2020-01-07 15:56:37.553991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74774f234d12'
down_revision = '625511d483c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('xxx', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cms_user', 'xxx')
    # ### end Alembic commands ###
