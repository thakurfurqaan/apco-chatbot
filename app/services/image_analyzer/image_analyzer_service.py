from fastapi import UploadFile

from app.core.image_analyzer import ImageAnalyzerInterface
from app.core.image_processor import ImageProcessorInterface
from app.core.image_recognizer_service import ImageRecognizer


class ImageAnalyzerService(ImageAnalyzerInterface):
    def __init__(
        self,
        image_processor: ImageProcessorInterface,
        image_recognizer: ImageRecognizer,
    ):
        self.image_processor = image_processor
        self.image_recognizer = image_recognizer

    def analyze(self, file: UploadFile) -> str:
        data_url = self.image_processor.get_data_url(file)
        return self.image_recognizer.recognize(image_url=data_url)
