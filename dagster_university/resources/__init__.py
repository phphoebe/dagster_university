from dagster_duckdb import DuckDBResource
from dagster import EnvVar

database_resource = DuckDBResource(
    # replaced with environment variable
    database=EnvVar("DUCKDB_DATABASE")
)
