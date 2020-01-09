"""empty message

Revision ID: 5e5891daa426
Revises: 914fd1e38099
Create Date: 2020-01-07 16:43:53.162808

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e5891daa426'
down_revision = '914fd1e38099'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cms_user', 'xxx')
    op.drop_column('cms_user', 'zzz')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('zzz', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('cms_user', sa.Column('xxx', mysql.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###
