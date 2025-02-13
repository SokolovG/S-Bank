from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """DataBase settings.

    All settings for Posters
    """
    DATABASE_URL: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def database_url(self) -> str:
        """Return database url."""
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'

    class Config:
        """Load env files"""
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
