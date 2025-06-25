from functools import lru_cache
import os
from backend.v1.app.core.config import DevelopmentSettings, ProductionSettings


@lru_cache()
def get_settings():
    env = os.getenv("ENVIRONMENT", "development").lower()

    if env == "production":
        return ProductionSettings()
    return DevelopmentSettings()