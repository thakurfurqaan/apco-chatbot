from abc import ABC, abstractmethod


class ImageRecognizer(ABC):

    @abstractmethod
    def recognize(self, image_url: str) -> str:
        """Recognize an image."""
        pass
