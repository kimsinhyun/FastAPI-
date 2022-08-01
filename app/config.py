from pydantic import BaseSettings
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCSES_TOKEN_EXPIRE_TIME: int

    class Config:
        env_file = ".env"


settings = Settings()
