import re
from typing import List

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    # Prefix that is appended to API routes and the docs.
    # E.g., with "/api" you can then call localhost:3001/api/
    API_ROOT: str = "/api"

    # Port where the API will listen
    API_PORT: int = 3001

    # Origins that are allowed to call the backend. Put in the URL
    # of the frontend if it has a different origin than the backend.
    CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("API_ROOT")
    def no_trailing_slashes_in_api_root(cls, value: str):
        return re.sub("/$", "", value)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
