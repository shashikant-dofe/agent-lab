from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def chat(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the language model.
        """
        raise NotImplementedError