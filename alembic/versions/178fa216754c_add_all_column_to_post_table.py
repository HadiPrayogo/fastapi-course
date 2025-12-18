"""add all column to post table

Revision ID: 178fa216754c
Revises: 0434555bc02d
Create Date: 2025-12-18 11:32:52.198573

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "178fa216754c"
down_revision: Union[str, Sequence[str], None] = "0434555bc02d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean, nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "published")
    op.drop_column("posts", "content")
    op.drop_column("posts", "created_at")
