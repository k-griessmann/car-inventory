"""empty message

Revision ID: a78bf589b5bc
Revises: 97bb5e69c2e2
Create Date: 2024-01-23 14:57:49.776157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a78bf589b5bc'
down_revision = '97bb5e69c2e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('make', sa.String(length=150), nullable=False),
    sa.Column('model', sa.String(length=200), nullable=True),
    sa.Column('year', sa.String(length=20), nullable=True),
    sa.Column('color', sa.String(length=200), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('user_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], name='contact_user_token_fkey'),
    sa.PrimaryKeyConstraint('id', name='contact_pkey')
    )
    op.drop_table('car')
    # ### end Alembic commands ###
