"""empty message

Revision ID: 2c1380b79145
Revises: ef9046ea9829
Create Date: 2022-01-05 11:44:14.787592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c1380b79145'
down_revision = 'ef9046ea9829'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('section', 'starts_at',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('section', 'ends_at',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('section', 'length',
               existing_type=sa.NUMERIC(),
               nullable=False)
    op.alter_column('section', 'user_fee',
               existing_type=sa.NUMERIC(),
               nullable=False)
    op.alter_column('section', 'max_speed',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('section', 'gauge',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('section', 'gauge',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('section', 'max_speed',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('section', 'user_fee',
               existing_type=sa.NUMERIC(),
               nullable=True)
    op.alter_column('section', 'length',
               existing_type=sa.NUMERIC(),
               nullable=True)
    op.alter_column('section', 'ends_at',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('section', 'starts_at',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
