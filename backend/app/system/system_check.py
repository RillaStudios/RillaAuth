from sqlmodel import SQLModel


class SystemHealthCheck(SQLModel, table=False):
    bootstrap_db_healthy: bool = False
    api_healthy: bool = False
    auth_db_healthy: bool = False
