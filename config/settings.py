"""
System Configuration Settings Module.

Manages application configurations loaded from active environmental contexts.
"""

import os
from functools import lru_cache
from typing import Optional

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    # Minimal fallback structure if pydantic-settings package is missing
    class BaseSettings:  # type: ignore
        def __init__(self) -> None:
            pass
    class SettingsConfigDict:  # type: ignore
        def __init__(self, *args, **kwargs) -> None:
            pass


class Settings(BaseSettings):
    """System-wide configuration settings loaded from environment or .env file."""

    # Pydantic Settings configuration parameters
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # General Configuration
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() in ("true", "1", "yes")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback-secret-key-for-dev")

    # Service Configuration
    BACKEND_HOST: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    BACKEND_PORT: int = int(os.getenv("BACKEND_PORT", "8000"))
    FRONTEND_PORT: int = int(os.getenv("FRONTEND_PORT", "5173"))

    # Database Configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "sqlite:///./autodev.db"
    )

    # LLM Settings
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "openai")
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    # MCP Configurations
    MCP_SERVER_CONFIG_PATH: str = os.getenv(
        "MCP_SERVER_CONFIG_PATH", "./config/mcp_servers.json"
    )
    MCP_TIMEOUT_SECONDS: int = int(os.getenv("MCP_TIMEOUT_SECONDS", "30"))


@lru_cache
def get_settings() -> Settings:
    """Retrieve cached instance of system configuration settings."""
    return Settings()
