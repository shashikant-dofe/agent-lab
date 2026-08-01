from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    app_name: str
    app_version: str
    environment: str
    log_level: str
    database_url: str
    llm_provider: str = "openai"
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"
    
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

settings = Settings()