"""add foregin-key to user table

Revision ID: 0434555bc02d
Revises: f87d8642f1b7
Create Date: 2025-12-18 11:23:38.449905

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0434555bc02d"
down_revision: Union[str, Sequence[str], None] = "f87d8642f1b7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
