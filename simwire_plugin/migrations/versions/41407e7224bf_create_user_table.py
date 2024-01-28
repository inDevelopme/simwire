"""Create User Table


Revision ID: 41407e7224bf
Revises:
Create Date: 2024-01-22 06:36:58.211131
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '41407e7224bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        # this circumvents an issue where username and email cannot be null but cannot be blank either
        sa.Column('username', sa.String(length=80), nullable=False, default='unknown@unknown.com'),
        sa.Column('email', sa.String(length=120), nullable=False, default='unknown@unknown.com'),
        sa.Column(
            'password',
            sa.String(length=200),
            nullable=False,
            default='$pbkdf2-sha256$29000$cs65N8a4d25tTamVEsJY6w$ajG1MzwCeEBdsVKqwyUo7gutByshm5rC7IrPIm6CXW4'
        ),
        sa.Column('nickname', sa.String(length=45)),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
