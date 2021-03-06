"""
Add full text search indexing for repo name and description.

Revision ID: e2894a3a3c19
Revises: d42c175b439a
Create Date: 2017-01-11 13:55:54.890774
"""

# revision identifiers, used by Alembic.
revision = "e2894a3a3c19"
down_revision = "d42c175b439a"

import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade(op, tables, tester):
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "repository_description__fulltext",
        "repository",
        ["description"],
        unique=False,
        postgresql_using="gin",
        postgresql_ops={"description": "gin_trgm_ops"},
        mysql_prefix="FULLTEXT",
    )
    op.create_index(
        "repository_name__fulltext",
        "repository",
        ["name"],
        unique=False,
        postgresql_using="gin",
        postgresql_ops={"name": "gin_trgm_ops"},
        mysql_prefix="FULLTEXT",
    )
    # ### end Alembic commands ###


def downgrade(op, tables, tester):
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("repository_name__fulltext", table_name="repository")
    op.drop_index("repository_description__fulltext", table_name="repository")
    # ### end Alembic commands ###
