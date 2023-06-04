"""empty message

Revision ID: 3da7f6534be3
Revises: 50ebf91dd306
Create Date: 2023-06-04 19:04:50.775988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3da7f6534be3'
down_revision = '50ebf91dd306'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ds_meta_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deposition_id', sa.Integer(), nullable=True))

    with op.batch_alter_table('fm_meta_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uvl_filename', sa.String(length=120), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fm_meta_data', schema=None) as batch_op:
        batch_op.drop_column('uvl_filename')

    with op.batch_alter_table('ds_meta_data', schema=None) as batch_op:
        batch_op.drop_column('deposition_id')

    # ### end Alembic commands ###