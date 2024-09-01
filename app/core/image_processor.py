from abc import ABC, abstractmethod

from fastapi import UploadFile


class ImageProcessorInterface(ABC):
    @abstractmethod
    async def get_data_url(self, file: UploadFile) -> str:
        pass
