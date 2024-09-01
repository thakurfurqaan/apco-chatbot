from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    file: Optional[UploadFile] = None


class ChatResponse(BaseModel):
    message: str


class ImageAnalysisRequest(BaseModel):
    file: UploadFile


class ImageAnalysisResponse(BaseModel):
    description: str
