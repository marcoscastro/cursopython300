"""empty message

Revision ID: 76345826c6b4
Revises: 
Create Date: 2017-01-25 01:31:01.819799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76345826c6b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aulas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=80), nullable=True),
    sa.Column('url', sa.String(length=50), nullable=True),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comentarios_aulas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('comentario', sa.Text(), nullable=True),
    sa.Column('id_aula', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_aula'], ['aulas.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comentarios_aulas')
    op.drop_table('aulas')
    # ### end Alembic commands ###
