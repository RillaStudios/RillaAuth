from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    """
    User model for the database.
    This model represents a user in the system.
    It includes fields for the user's ID, username, email, password,
    disabled status, and superuser status.

    Attributes:
        id (int | None): The unique identifier for the user. Defaults to None.
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
        disabled (bool): Indicates if the user is disabled. Defaults to False.
        is_superuser (bool): Indicates if the user has superuser privileges. Defaults to False.

    Methods:
        __repr__(): Returns a string representation of the User object.

    This model is used in conjunction with SQLModel to interact with the database.
    It is important to note that the password should be hashed before being stored in the database.

    @author IFD
    @date 2025-05-01
    """

    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    disabled: bool = False
    is_superuser: bool = False

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, email={self.email})"