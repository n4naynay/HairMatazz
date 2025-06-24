from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from typing import Optional, Literal


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")  # default fallback

    ENVIRONMENT: Literal["development", "staging", "production"] = "development"

    PROJECT_NAME: str = "HairMatazz"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    CORS_ORIGINS: list[str] = ["*"]

    SECRET_KEY: SecretStr
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES: int = 60
    CHANGE_PASSWORD_TOKEN_EXPIRE_MINUTES: int = 30

    JWT_ALGORITHM: str = "HS256"
    JWT_AUDIENCE: str = "hairmatazz:auth"
    JWT_TOKEN_PREFIX: str = "Bearer"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_SERVER: str
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str
    DATABASE_URL: Optional[str] = None

    @property
    def assembled_db_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD.get_secret_value()}@"
            f"{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class DevelopmentSettings(BaseAppSettings):
    model_config = SettingsConfigDict(env_file=".env.development")
    CORS_ORIGINS: list[str] = ["http://localhost:8000"]


class ProductionSettings(BaseAppSettings):
    model_config = SettingsConfigDict(env_file=".env.production")
    CORS_ORIGINS: list[str] = ["https://myapp.com"]