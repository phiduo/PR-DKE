"""empty message

Revision ID: 3f80e6b3fd40
Revises: cbc663cbb80f
Create Date: 2022-01-18 08:06:42.797993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f80e6b3fd40'
down_revision = 'cbc663cbb80f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('railway', schema=None) as batch_op:
        batch_op.drop_constraint('disjoint_stations', type_='unique')
        batch_op.create_unique_constraint('UQ_starts_at_ends_at', ['starts_at', 'ends_at'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('railway', schema=None) as batch_op:
        batch_op.drop_constraint('UQ_starts_at_ends_at', type_='unique')
        batch_op.create_unique_constraint('disjoint_stations', ['starts_at', 'ends_at'])

    # ### end Alembic commands ###
