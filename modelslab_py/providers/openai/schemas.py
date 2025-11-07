from typing import Optional
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class Sora2Schema(BaseSchema):
    """Schema for OpenAI Sora 2 Text-to-Video (sora-2)"""

    model_id: str = Field(
        default="sora-2",
        description="Model ID: sora-2"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    aspect_ratio: Optional[str] = Field(
        None,
        description="Video aspect ratio (16:9, 9:16)"
    )
    duration: Optional[str] = Field(
        None,
        description="Video duration (4s, 8s, 12s)"
    )
