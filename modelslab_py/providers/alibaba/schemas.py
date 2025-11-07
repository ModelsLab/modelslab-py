from typing import Optional, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class Wan25I2VSchema(BaseSchema):
    """Schema for Alibaba Wan 2.5 Image-to-Video (wan2.5-i2v)"""

    model_id: str = Field(
        default="wan2.5-i2v",
        description="Model ID: wan2.5-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Image to convert to video"
    )
    init_audio: Any = Field(
        ...,
        description="Audio file (WAV/MP3, truncates to 5-10 seconds)"
    )
    prompt: str = Field(
        ...,
        description="Describes desired video actions and scene"
    )


class Wan25T2VSchema(BaseSchema):
    """Schema for Alibaba Wan 2.5 Text-to-Video (wan2.5-t2v)"""

    model_id: str = Field(
        default="wan2.5-t2v",
        description="Model ID: wan2.5-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    init_audio: Any = Field(
        ...,
        description="Audio file URL or path"
    )
    enhance_prompt: Optional[bool] = Field(
        None,
        description="Enable prompt rewriting"
    )
    generate_audio: Optional[bool] = Field(
        None,
        description="Generate audio for video"
    )
