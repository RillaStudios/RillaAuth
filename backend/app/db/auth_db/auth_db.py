from typing import Generator, Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel
from app.config import settings

engine = create_engine(settings.DB_URL, echo=True)

def init_db():
    """
    Initialize the database by creating all tables defined in SQLModel models.
    This function should be called at the start of the application to ensure
    that the database schema is up to date with the models defined in the codebase.
    It uses the SQLModel's metadata to create all tables in the database.
    The `echo=True` parameter in the create_engine function enables logging of
    all SQL statements executed, which is useful for debugging and monitoring
    database interactions.

    @author IFD
    @date 2025-05-01

    :return:
    """

    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """
    Get a new SQLAlchemy session for database operations.
    This function is a generator that yields a session object. It should be used
    within a context manager to ensure that the session is properly closed
    after use. The session object can be used to perform database operations
    such as querying, inserting, updating, and deleting records. The session
    is created using the SQLModel's create_engine function, which connects to
    the database specified in the configuration settings. The `echo=True`
    parameter in the create_engine function enables logging of all SQL
    statements executed, which is useful for debugging and monitoring
    database interactions.

    @author IFD
    @date 2025-05-01

    :return:
    """
    with Session(engine) as session:
        yield session

AuthDbSession = Annotated[Session, Depends(get_session)]