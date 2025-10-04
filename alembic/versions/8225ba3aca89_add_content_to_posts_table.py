"""add content to posts table

Revision ID: 8225ba3aca89
Revises: c65d91418b34
Create Date: 2025-10-02 23:53:09.558270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8225ba3aca89'
down_revision: Union[str, Sequence[str], None] = 'c65d91418b34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
