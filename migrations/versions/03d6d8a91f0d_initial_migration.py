"""Initial migration.

Revision ID: 03d6d8a91f0d
Revises: e5638e55e8f8
Create Date: 2020-04-07 15:42:39.810202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03d6d8a91f0d'
down_revision = 'e5638e55e8f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('alamat', table_name='user')
    op.drop_index('kelas', table_name='user')
    op.drop_index('nama', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('nama', 'user', ['nama'], unique=True)
    op.create_index('kelas', 'user', ['kelas'], unique=True)
    op.create_index('alamat', 'user', ['alamat'], unique=True)
    # ### end Alembic commands ###