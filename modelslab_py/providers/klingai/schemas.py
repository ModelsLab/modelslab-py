from typing import Optional, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class KlingV21I2VSchema(BaseSchema):
    """Schema for Kling V2.1 Image-to-Video (kling-v2-1-i2v)"""

    model_id: str = Field(
        default="kling-v2-1-i2v",
        description="Model ID: kling-v2-1-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: str = Field(
        ...,
        description="Video duration: 5 or 10 seconds"
    )


class KlingV25TurboI2VSchema(BaseSchema):
    """Schema for Kling V2.5 Turbo Image-to-Video (Kling-V2-5-Turbo-i2v)"""

    model_id: str = Field(
        default="Kling-V2-5-Turbo-i2v",
        description="Model ID: Kling-V2-5-Turbo-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: str = Field(
        ...,
        description="Video duration: 5 or 10 seconds"
    )


class KlingV25TurboT2VSchema(BaseSchema):
    """Schema for Kling V2.5 Turbo Text-to-Video (kling-v2-5-turbo-t2v)"""

    model_id: str = Field(
        default="kling-v2-5-turbo-t2v",
        description="Model ID: kling-v2-5-turbo-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: str = Field(
        ...,
        description="Video duration: 5 or 10 seconds"
    )
    aspect_ratio: str = Field(
        ...,
        description="Video aspect ratio: 16:9, 9:16, or 1:1"
    )


class KlingV2MasterT2VSchema(BaseSchema):
    """Schema for Kling V2 Master Text-to-Video (kling-v2-master-t2v)"""

    model_id: str = Field(
        default="kling-v2-master-t2v",
        description="Model ID: kling-v2-master-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: str = Field(
        ...,
        description="Video duration: 5 or 10 seconds"
    )


class KlingV2MasterI2VSchema(BaseSchema):
    """Schema for Kling V2 Master Image-to-Video (kling-v2-master-i2v)"""

    model_id: str = Field(
        default="kling-v2-master-i2v",
        description="Model ID: kling-v2-master-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: str = Field(
        ...,
        description="Video duration: 5 or 10 seconds"
    )


class KlingV21MasterT2VSchema(BaseSchema):
    """Schema for Kling V2.1 Master Text-to-Video (kling-v2-1-master-t2v)"""

    model_id: str = Field(
        default="kling-v2-1-master-t2v",
        description="Model ID: kling-v2-1-master-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: str = Field(
        ...,
        description="Video duration: 5 or 10 seconds"
    )


class KlingV21MasterI2VSchema(BaseSchema):
    """Schema for Kling V2.1 Master Image-to-Video (kling-v2-1-master-i2v)"""

    model_id: str = Field(
        default="kling-v2-1-master-i2v",
        description="Model ID: kling-v2-1-master-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: str = Field(
        ...,
        description="Video duration: 5 or 10 seconds"
    )
