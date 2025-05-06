import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

class Settings:
    """
    Settings class to manage application configuration.
    Loads environment variables from a .env file and provides default values.

    Attributes:
        APP_NAME (str): Name of the application.
        APP_DESCRIPTION (str): Description of the application.
        APP_VERSION (str): Version of the application.
        DB_NAME (str): Database name.
        DB_USER (str): Database user.
        DB_PASSWORD (str): Database password.
        DB_HOST (str): Database host.
        DB_PORT (int): Database port.
        DB_URL (str): Database connection URL.
        CORS_ORIGINS (list): List of allowed CORS origins.
        CORS_ALLOW_CREDENTIALS (bool): Allow credentials in CORS requests.
        CORS_ALLOW_METHODS (list): Allowed HTTP methods for CORS requests.
        CORS_ALLOW_HEADERS (list): Allowed headers for CORS requests.
        CORS_EXPOSE_HEADERS (list): Exposed headers for CORS responses.
        CORS_MAX_AGE (int): Maximum age for CORS preflight requests.
        SECRET_KEY (str): Secret key for JWT signing.
        ALGORITHM (str): Algorithm used for JWT signing.
        ACCESS_TOKEN_EXPIRE_MINUTES (float): Expiration time for access tokens in minutes.
        AUTH_SCHEME (OAuth2PasswordBearer): OAuth2 password bearer scheme for token authentication.

    @author IFD
    @date 2025-05-01
    """

    # Application settings
    APP_NAME: str = os.getenv("APP_NAME", "RillaAuth")
    APP_DESCRIPTION: str = os.getenv("APP_DESCRIPTION", "RillaAuth")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.0.1")

    # Database settings
    DB_NAME: str = os.getenv("DB_NAME", "rillaauth_db")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 3306))
    DB_URL: str = os.getenv("DB_URL") or f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Cors settings
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "*").split(",")
    CORS_ALLOW_CREDENTIALS: bool = os.getenv("CORS_ALLOW_CREDENTIALS", "true").lower() == "true"
    CORS_ALLOW_METHODS: list = os.getenv("CORS_ALLOW_METHODS", "*").split(",")
    CORS_ALLOW_HEADERS: list = os.getenv("CORS_ALLOW_HEADERS", "*").split(",")
    CORS_EXPOSE_HEADERS: list = os.getenv("CORS_EXPOSE_HEADERS", "*").split(",")
    CORS_MAX_AGE: int = int(os.getenv("CORS_MAX_AGE", 3600))

    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: float = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # OAuth2 settings
    AUTH_SCHEME = OAuth2PasswordBearer(tokenUrl="token")


settings = Settings()