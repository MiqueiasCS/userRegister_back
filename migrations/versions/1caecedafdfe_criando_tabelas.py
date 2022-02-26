"""criando tabelas

Revision ID: 1caecedafdfe
Revises: 
Create Date: 2022-02-26 20:16:52.929227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1caecedafdfe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cep', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('street', sa.String(), nullable=False),
    sa.Column('House_number', sa.Integer(), nullable=False),
    sa.Column('complement', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    op.drop_table('user')
    # ### end Alembic commands ###