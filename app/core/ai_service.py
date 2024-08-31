from abc import ABC, abstractmethod


class AIService(ABC):
    @abstractmethod
    def process_prompt(self, prompt: str) -> str:
        pass
