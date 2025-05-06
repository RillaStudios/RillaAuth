from sqlmodel import SQLModel, Field

"""
Token and TokenData models for storing access tokens and token data.
These models are used to manage user authentication and authorization
in an application.

The Token model stores the access token and its type, while the
TokenData model stores additional information about the token,
such as the associated username.

@author IFD
@date 2025-05-01
"""

class Token(SQLModel, table=True):
    """
    Token model for storing access tokens and their type.
    This model is used to manage user authentication and authorization
    in an application.

    Attributes:
        id (int): Unique identifier for the token.
        access_token (str): The access token string.
        token_type (str): The type of the token (e.g., "bearer").

    @author IFD
    @date 2025-05-01
    """

    __tablename__ = "tokens"

    id: int = Field(default=None, primary_key=True)
    access_token: str
    token_type: str

class TokenData(SQLModel, table=True):
    """
    TokenData model for storing additional information about the token.
    This model is used to manage user authentication and authorization
    in an application.

    Attributes:
        id (int): Unique identifier for the token data.
        username (str | None): The username associated with the token.

    @author IFD
    @date 2025-05-01
    """

    __tablename__ = "token_data"

    id: int = Field(default=None, primary_key=True)
    username: str | None = None