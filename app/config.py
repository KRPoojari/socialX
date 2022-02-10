from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    database_hostname: Optional[str]
    database_port: Optional[str]
    database_password: Optional[str]
    database_name: Optional[str]
    database_username: Optional[str]
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    database_url: Optional[str]

    class Config:
        env_file = ".env"

settings = Settings()