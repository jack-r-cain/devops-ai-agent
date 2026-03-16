from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Provide a default so static checkers don't require it at instantiation;
    # the value will still be overridden from the environment/.env at runtime.
    openai_api_key: str = ""
    triage_model: str = "gpt-5-mini"
    solution_model: str = "gpt-5.4"
    evaluator_model: str = "gpt-5.4"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()