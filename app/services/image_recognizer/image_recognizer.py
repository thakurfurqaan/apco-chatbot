from app.core.image_recognizer_service import ImageRecognizer


class GPT4Image(ImageRecognizer):
    async def recognize(self, image_data: bytes) -> str:
        # Implement GPT-4 Vision API call here
        pass
