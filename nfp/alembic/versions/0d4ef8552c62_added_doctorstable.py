"""Added doctorstable

Revision ID: 0d4ef8552c62
Revises: d7ea55450205
Create Date: 2022-12-02 15:02:17.099762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d4ef8552c62'
down_revision = 'd7ea55450205'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctors', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('doctors', sa.Column('title', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('email', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('street', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('city', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('state', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('postal', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('site_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctors', 'site_id')
    op.drop_column('doctors', 'postal')
    op.drop_column('doctors', 'state')
    op.drop_column('doctors', 'city')
    op.drop_column('doctors', 'street')
    op.drop_column('doctors', 'email')
    op.drop_column('doctors', 'phone')
    op.drop_column('doctors', 'first_name')
    op.drop_column('doctors', 'last_name')
    op.drop_column('doctors', 'title')
    op.drop_column('doctors', 'id')
    # ### end Alembic commands ###
