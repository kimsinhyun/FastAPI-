from pydantic import BaseSettings
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABSE_HOSTNAME: str
    DATABSE_PORT: str
    DATABSE_PASSWORD: str
    DATABSE_NAME: str
    DATABSE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCSES_TOKEN_EXPIRE_TIME: int

    class Config:
        env_file = ".env"


settings = Settings()
