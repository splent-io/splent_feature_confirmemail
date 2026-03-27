"""Alembic migration environment for splent_feature_confirmemail."""

from splent_io.splent_feature_confirmemail import models  # noqa: F401
from splent_framework.migrations.feature_env import run_feature_migrations

FEATURE_NAME = "splent_feature_confirmemail"
FEATURE_TABLES = {"confirmemail"}

run_feature_migrations(FEATURE_NAME, FEATURE_TABLES)
