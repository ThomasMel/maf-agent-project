import os

from autogen_ext.models.openai import OpenAIChatCompletionClient
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Dynamically picks up environment variables or defaults to a mock string
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "mock-key")
    model_name: str = "gpt-4o"


settings = Settings()


def get_llm_client() -> OpenAIChatCompletionClient:
    """Returns a configured Microsoft AutoGen LLM client link."""
    return OpenAIChatCompletionClient(
        model=settings.model_name, api_key=settings.openai_api_key
    )
