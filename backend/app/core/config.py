from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    app_name: str = "StudyHub API"
    app_version: str = "1.0.0"
    environment: str = "development"
    debug: bool = False
    
    # Supabase (Auth, Storage, Edge)
    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_role_key: str = ""
    
    # Database (PostgreSQL via asyncpg or SQLite fallback)
    database_url: str = "sqlite+aiosqlite:///./pathward.db"
    
    # Groq LLM
    llm_provider: str = "groq"
    groq_api_key: str = ""
    groq_model: str = "llama3-70b-8192"
    
    # CORS
    frontend_url: str = "http://localhost:3000"
    additional_cors_origins: str = ""

    @property
    def is_production(self) -> bool:
        return self.environment.lower() in ("production", "prod")

    @property
    def cors_origins(self) -> List[str]:
        origins = [
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:3001",
            "http://127.0.0.1:3001",
        ]
        if self.frontend_url and self.frontend_url not in origins:
            origins.append(self.frontend_url)
        if self.additional_cors_origins:
            for extra in self.additional_cors_origins.split(","):
                clean = extra.strip()
                if clean and clean not in origins:
                    origins.append(clean)
        return origins
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
