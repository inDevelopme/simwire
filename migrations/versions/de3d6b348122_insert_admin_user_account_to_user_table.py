"""Insert admin user account to user table.

Revision ID: de3d6b348122
Revises: 41407e7224bf
Create Date: 2024-01-22 08:27:21.230589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de3d6b348122'
down_revision = '41407e7224bf'
branch_labels = None
depends_on = None


def upgrade():
    # Seed data
    users = [
        {
            'username': 'testing@testing.com',
            'email': 'testing@testing.com',
            'password': '$pbkdf2-sha256$29000$cs65N8a4d25tTamVEsJY6w$ajG1MzwCeEBdsVKqwyUo7gutByshm5rC7IrPIm6CXW4'
        },
    ]

    op.bulk_insert(
        # Table to be updated
        sa.Table(
            'users',
            sa.MetaData(),
            autoload_with=op.get_bind()
        ),
        # dictionary of data to be inserted
        users
    )


def downgrade():
    op.execute("DELETE FROM user WHERE username='testing@testing.com'")
