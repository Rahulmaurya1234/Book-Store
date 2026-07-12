from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.aws_secrets import get_secret


aws_secret = get_secret("book-store-secrets")


class Settings(BaseSettings):

    APP_NAME: str = "Book Store API"
    APP_VERSION: str = "1.0.0"

    DB_HOST: str = aws_secret["DB_HOST"]
    DB_PORT: int = int(aws_secret["DB_PORT"])
    DB_NAME: str = aws_secret["DB_NAME"]
    DB_USER: str = aws_secret["DB_USER"]
    DB_PASSWORD: str = aws_secret["DB_PASSWORD"]

    SECRET_KEY: str = aws_secret["SECRET_KEY"]
    ALGORITHM: str = aws_secret["ALGORITHM"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        aws_secret["ACCESS_TOKEN_EXPIRE_MINUTES"]
    )

    model_config = SettingsConfigDict(
        extra="ignore",
    )


settings = Settings()