from abc import ABC, abstractmethod


class ImageRecognizer(ABC):
    @abstractmethod
    async def recognize(self, image_data: bytes) -> dict:
        pass
