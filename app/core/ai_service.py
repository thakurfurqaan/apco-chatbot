from abc import ABC, abstractmethod


class AIService(ABC):
    @abstractmethod
    async def process_prompt(self, prompt: str) -> str:
        pass
