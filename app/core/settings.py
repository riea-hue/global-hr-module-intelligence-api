from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Global HR Intelligence API"
    VERSION: str = "1.0.0"
    PROVIDER: str = "memory"
    DEBUG: bool = True


settings = Settings()
