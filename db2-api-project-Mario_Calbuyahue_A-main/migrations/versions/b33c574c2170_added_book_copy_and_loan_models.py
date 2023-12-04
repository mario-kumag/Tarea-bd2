"""Added book copy and loan models

Revision ID: b33c574c2170
Revises: 9b2a6fc8178c
Create Date: 2023-12-03 13:18:02.063346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b33c574c2170'
down_revision: Union[str, None] = '9b2a6fc8178c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_copies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_copy_id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('loaned_date', sa.DateTime(), nullable=False),
    sa.Column('return_date', sa.DateTime(), nullable=False),
    sa.Column('returned_date', sa.DateTime(), nullable=False),
    sa.Column('penalty', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_copy_id'], ['book_copies.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['Client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('loans')
    op.drop_table('book_copies')
    # ### end Alembic commands ###