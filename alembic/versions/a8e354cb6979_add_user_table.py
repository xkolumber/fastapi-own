"""add user table

Revision ID: a8e354cb6979
Revises: 8225ba3aca89
Create Date: 2025-10-03 10:22:02.906468

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8e354cb6979'
down_revision: Union[str, Sequence[str], None] = '8225ba3aca89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False, unique=True),
        sa.Column('password', sa.String(length=128), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone = True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
