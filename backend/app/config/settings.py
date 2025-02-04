import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()

class Settings(BaseSettings):
    ENVIRONMENT: str = 'local'
    DB_HOST: str = 'localhost'
    DB_PORT: int = os.getenv('DB_PORT')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASS: str = os.getenv('DB_PASSWORD')
    DB_NAME: str = os.getenv('DB_NAME')

    @property
    def database_url(self) -> str:
        if self.ENVIRONMENT == 'local':
            host = 'localhost'
        else:
            host = 'db'
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{host}:{self.DB_PORT}/{self.DB_NAME}'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()