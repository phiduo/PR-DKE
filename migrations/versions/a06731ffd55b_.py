"""empty message

Revision ID: a06731ffd55b
Revises: 3a29570a16eb
Create Date: 2022-01-18 13:33:15.494106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a06731ffd55b'
down_revision = '3a29570a16eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('railway', schema=None) as batch_op:
        batch_op.drop_constraint('UQ_starts_at_ends_at', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('railway', schema=None) as batch_op:
        batch_op.create_unique_constraint('UQ_starts_at_ends_at', ['starts_at', 'ends_at'])

    # ### end Alembic commands ###
