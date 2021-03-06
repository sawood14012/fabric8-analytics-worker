"""Drop BigQuery results table.

Revision ID: 43360d9467b9
Revises: 727aeeb88b2f
Create Date: 2018-05-22 10:58:32.130995

"""

# revision identifiers, used by Alembic.
revision = '43360d9467b9'
down_revision = '727aeeb88b2f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('component_gh_usage')
    op.drop_table('package_gh_usage')
    op.alter_column('osio_registered_repos', 'git_sha',
                    existing_type=sa.TEXT(),
                    type_=sa.String(length=255),
                    existing_nullable=False)
    op.create_index(op.f('ix_versions_synced2graph'), 'versions', ['synced2graph'], unique=False)
    op.drop_index('ix_synced2graph', table_name='versions')
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_synced2graph', 'versions', ['synced2graph'], unique=False)
    op.drop_index(op.f('ix_versions_synced2graph'), table_name='versions')
    op.alter_column('osio_registered_repos', 'git_sha',
                    existing_type=sa.String(length=255),
                    type_=sa.TEXT(),
                    existing_nullable=False)
    op.create_table('package_gh_usage',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
                    sa.Column('count', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('ecosystem_backend',
                              postgresql.ENUM('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm',
                                              'crates', 'nuget', name='ecosystem_backend_enum'),
                              autoincrement=False, nullable=True),
                    sa.Column('timestamp', postgresql.TIMESTAMP(),
                              server_default=sa.text("('now'::text)::timestamp without time zone"),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='package_gh_usage_pkey')
                    )
    op.create_table('component_gh_usage',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
                    sa.Column('version', sa.VARCHAR(length=255), autoincrement=False,
                              nullable=False),
                    sa.Column('count', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('ecosystem_backend',
                              postgresql.ENUM('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm',
                                              'crates', 'nuget', name='ecosystem_backend_enum'),
                              autoincrement=False, nullable=True),
                    sa.Column('timestamp', postgresql.TIMESTAMP(),
                              server_default=sa.text("('now'::text)::timestamp without time zone"),
                              autoincrement=False, nullable=False),
                    sa.Column('percentile_rank', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='component_gh_usage_pkey')
                    )
    # ### end Alembic commands ###
