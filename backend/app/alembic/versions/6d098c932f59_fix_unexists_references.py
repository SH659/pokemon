"""fix unexists references

Revision ID: 6d098c932f59
Revises: dec7d96d5844
Create Date: 2021-06-26 19:05:56.603512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d098c932f59'
down_revision = 'dec7d96d5844'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('picture_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pokemon_id'), 'pokemon', ['id'], unique=False)
    op.create_index(op.f('ix_pokemon_name'), 'pokemon', ['name'], unique=False)
    op.create_table('user_pokemon',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('pokemon', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pokemon'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_pokemon_id'), 'user_pokemon', ['id'], unique=False)
    op.create_index(op.f('ix_user_pokemon_pokemon'), 'user_pokemon', ['pokemon'], unique=False)
    op.create_index(op.f('ix_user_pokemon_user'), 'user_pokemon', ['user'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_pokemon_user'), table_name='user_pokemon')
    op.drop_index(op.f('ix_user_pokemon_pokemon'), table_name='user_pokemon')
    op.drop_index(op.f('ix_user_pokemon_id'), table_name='user_pokemon')
    op.drop_table('user_pokemon')
    op.drop_index(op.f('ix_pokemon_name'), table_name='pokemon')
    op.drop_index(op.f('ix_pokemon_id'), table_name='pokemon')
    op.drop_table('pokemon')
    # ### end Alembic commands ###