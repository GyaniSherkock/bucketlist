"""empty message

Revision ID: 4042d1aa102e
Revises: 5195759d1d3c
Create Date: 2020-07-22 21:45:51.827944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4042d1aa102e'
down_revision = '5195759d1d3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login_details',
    sa.Column('user_email', sa.String(length=128), nullable=False),
    sa.Column('user_password', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['user_email'], ['user_table.user_email'], ),
    sa.PrimaryKeyConstraint('user_email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('login_details')
    # ### end Alembic commands ###
