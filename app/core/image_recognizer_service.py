from abc import ABC, abstractmethod


class ImageRecognizer(ABC):

    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    @abstractmethod
    async def recognize(self, image_data: bytes) -> str:
        """Recognize an image."""
        pass
