from app.ai.openai_provider import OpenAIProvider
from app.ai.ollama_provider import OllamaProvider
from app.core.config import settings


class LLMFactory:

    @staticmethod
    def create():

        provider = settings.llm_provider.lower()

        if provider == "openai":
            return OpenAIProvider()

        if provider == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )