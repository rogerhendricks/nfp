"""Added chamber colum table

Revision ID: d7ea55450205
Revises: c5b22615e648
Create Date: 2022-12-02 09:06:06.063688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7ea55450205'
down_revision = 'c5b22615e648'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leads', sa.Column('chamber', sa.String(), nullable=True))
    op.drop_column('leads', 'dev_type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leads', sa.Column('dev_type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('leads', 'chamber')
    # ### end Alembic commands ###