from typing import Optional

from fastapi import File, UploadFile
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    file: Optional[UploadFile] = None


class ChatResponse(BaseModel):
    message: str


class ImageAnalysisRequest(BaseModel):
    file: UploadFile = File(...)


class ImageAnalysisResponse(BaseModel):
    description: str
