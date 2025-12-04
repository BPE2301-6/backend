"""add hashed_password to users

Revision ID: 9227af72b1e5
Revises: 85c0c9db9d8d
Create Date: 2025-12-04 19:44:28.421518+00:00

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9227af72b1e5"
down_revision: str | Sequence[str] | None = "85c0c9db9d8d"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('usr', sa.Column('hashed_password', sa.String(length=255), nullable=False))



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('usr', 'hashed_password')
