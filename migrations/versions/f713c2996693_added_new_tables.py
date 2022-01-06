"""Added new tables

Revision ID: f713c2996693
Revises: 5959f449803c
Create Date: 2022-01-05 03:57:18.479241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f713c2996693'
down_revision = '5959f449803c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('warnings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('starts_at', sa.Integer(), nullable=True),
    sa.Column('ends_at', sa.Integer(), nullable=True),
    sa.Column('length', sa.Numeric(), nullable=True),
    sa.Column('user_fee', sa.Numeric(), nullable=True),
    sa.Column('max_speed', sa.Integer(), nullable=True),
    sa.Column('gauge', sa.Integer(), nullable=True),
    sa.Column('railway_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ends_at'], ['stations.id'], ),
    sa.ForeignKeyConstraint(['railway_id'], ['railways.id'], ),
    sa.ForeignKeyConstraint(['starts_at'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('section')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('section',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('length', sa.NUMERIC(), nullable=True),
    sa.Column('user_fee', sa.NUMERIC(), nullable=True),
    sa.Column('max_speed', sa.INTEGER(), nullable=True),
    sa.Column('gauge', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sections')
    op.drop_table('warnings')
    # ### end Alembic commands ###