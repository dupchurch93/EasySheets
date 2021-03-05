"""create other models

Revision ID: 8bf7eb5e598d
Revises: ffdc0a98111c
Create Date: 2021-03-03 17:04:30.016804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bf7eb5e598d'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('source', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('race', sa.String(length=50), nullable=False),
    sa.Column('characterClass', sa.String(length=50), nullable=False),
    sa.Column('subclass', sa.String(length=100), nullable=True),
    sa.Column('imgURL', sa.String(length=256), nullable=True),
    sa.Column('proficiencies', sa.String(length=1000), nullable=False),
    sa.Column('background', sa.String(length=50), nullable=False),
    sa.Column('alignment', sa.String(length=50), nullable=False),
    sa.Column('attributes', sa.String(length=100), nullable=False),
    sa.Column('personality', sa.String(length=1000), nullable=False),
    sa.Column('inventory', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('languages', sa.String(length=500), nullable=True),
    sa.Column('tools', sa.String(500), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('characterAbilities',
    sa.Column('characterId', sa.Integer(), nullable=False),
    sa.Column('abilityId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['abilityId'], ['abilities.id'], ),
    sa.ForeignKeyConstraint(['characterId'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('characterId', 'abilityId')
    )
    op.create_table('characterTags',
    sa.Column('characterId', sa.Integer(), nullable=False),
    sa.Column('tagId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['characterId'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['tagId'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('characterId', 'tagId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('characterTags')
    op.drop_table('characterAbilities')
    op.drop_table('characters')
    op.drop_table('tags')
    op.drop_table('abilities')
    # ### end Alembic commands ###
