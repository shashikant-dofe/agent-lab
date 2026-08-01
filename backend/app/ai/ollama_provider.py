from app.ai.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):

    def chat(
        self,
        prompt: str,
    ) -> str:

        raise NotImplementedError(
            "Ollama provider not implemented yet."
        )