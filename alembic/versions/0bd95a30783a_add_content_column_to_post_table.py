"""add content column to post table

Revision ID: 0bd95a30783a
Revises: 4c654ebf156a
Create Date: 2025-07-04 12:22:39.600237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bd95a30783a'
down_revision: Union[str, Sequence[str], None] = '4c654ebf156a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
