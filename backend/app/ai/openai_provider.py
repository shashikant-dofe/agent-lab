from app.ai.base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):

    def chat(
        self,
        prompt: str,
    ) -> str:

        raise NotImplementedError(
            "OpenAI provider not implemented yet."
        )