"""add column to post table

Revision ID: f87d8642f1b7
Revises: 423d84d4bf36
Create Date: 2025-12-18 11:15:42.363182

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f87d8642f1b7"
down_revision: Union[str, Sequence[str], None] = "423d84d4bf36"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("title", sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "title")
    pass
