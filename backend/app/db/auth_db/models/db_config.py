from sqlmodel import SQLModel

class DbConfig(SQLModel, table=True):
    host: str
    port: int
    username: str
    password: str
    db_name: str