import base64

from fastapi import UploadFile

from app.core.image_processor import ImageProcessorInterface


class Base64ImageProcessor(ImageProcessorInterface):
    async def get_data_url(self, file: UploadFile) -> str:
        contents = await file.read()
        base64_encoded = base64.b64encode(contents).decode("utf-8")
        mime_type = file.content_type or "application/octet-stream"
        return f"data:{mime_type};base64,{base64_encoded}"
