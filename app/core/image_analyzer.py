from abc import ABC, abstractmethod

from fastapi import UploadFile


class ImageAnalyzerInterface(ABC):
    """Interface for image analyzer."""

    @abstractmethod
    def analyze(self, file: UploadFile) -> str:
        """Analyze the given image file and return a string description."""
        pass
