import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    ENVIRONMENT: str = 'local'
    SECRET_KEY: str
    DB_HOST: str = os.getenv('DB_HOST', 'localhost')
    DB_PORT: int = int(os.getenv('DB_PORT', 5432))
    DB_USER: str = os.getenv('DB_USER', 'postgres')
    DB_PASS: str = os.getenv('DB_PASSWORD', 'postgres')
    DB_NAME: str = os.getenv('DB_NAME', 'dev_events')

    @property
    def database_url(self) -> str:
        """Return database url."""
        host = 'localhost' if self.ENVIRONMENT == 'local' else 'db'
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{host}:{self.DB_PORT}/{self.DB_NAME}'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
