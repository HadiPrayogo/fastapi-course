"""create post table

Revision ID: 18c265dc09fe
Revises:
Create Date: 2025-12-18 10:11:18.142595

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "18c265dc09fe"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
