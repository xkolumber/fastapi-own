"""add phone number

Revision ID: 3fe7d022b8db
Revises: f4e2edc017f8
Create Date: 2025-10-03 15:50:01.021738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fe7d022b8db'
down_revision: Union[str, Sequence[str], None] = 'f4e2edc017f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
