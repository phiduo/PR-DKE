"""empty message

Revision ID: 2fa24ce3f6ac
Revises: 720064206f91
Create Date: 2022-01-16 07:46:31.610190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fa24ce3f6ac'
down_revision = '720064206f91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warning', sa.Column('description', sa.String(length=255), nullable=True))
    op.drop_constraint(None, 'warning', type_='foreignkey')
    op.drop_column('warning', 'section_id')
    op.drop_column('warning', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('warning', sa.Column('name', sa.VARCHAR(length=255), nullable=False))
    op.add_column('warning', sa.Column('section_id', sa.INTEGER(), nullable=False))
    op.create_foreign_key(None, 'warning', 'section', ['section_id'], ['id'])
    op.drop_column('warning', 'description')
    # ### end Alembic commands ###
