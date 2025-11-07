from typing import Optional, List, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class SeeDreamT2ISchema(BaseSchema):
    """Schema for SeeDream Text-to-Image (seedream-t2i)"""

    model_id: str = Field(
        default="seedream-t2i",
        description="Model ID: seedream-t2i"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    width: int = Field(
        ...,
        description="Image width (512-1024 pixels)"
    )
    height: int = Field(
        ...,
        description="Image height (512-1024 pixels)"
    )


class SeeDanceT2VSchema(BaseSchema):
    """Schema for SeeDance Text-to-Video (seedance-t2v)"""

    model_id: str = Field(
        default="seedance-t2v",
        description="Model ID: seedance-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    aspect_ratio: Optional[str] = Field(
        None,
        description="Aspect ratio options: 16:9, 4:3, 1:1, 9:21"
    )
    resolution: Optional[str] = Field(
        None,
        description="Resolution options: 720p, 480p"
    )
    camera_fixed: Optional[bool] = Field(
        None,
        description="Control camera positioning (true/false)"
    )


class SeeDanceI2VSchema(BaseSchema):
    """Schema for SeeDance Image-to-Video (seedance-i2v)"""

    model_id: str = Field(
        default="seedance-i2v",
        description="Model ID: seedance-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image (file/URL)"
    )
    prompt: str = Field(
        ...,
        description="Descriptive text for video generation"
    )


class SeeEditI2ISchema(BaseSchema):
    """Schema for SeeEdit Image-to-Image (seededit-i2i)"""

    model_id: str = Field(
        default="seededit-i2i",
        description="Model ID: seededit-i2i"
    )
    init_image: Any = Field(
        ...,
        description="Source image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description of desired image transformation"
    )


class SeeDream4Schema(BaseSchema):
    """Schema for SeeDream 4 Text-to-Image (seedream-4)"""

    model_id: str = Field(
        default="seedream-4",
        description="Model ID: seedream-4"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    aspect_ratio: str = Field(
        ...,
        description="Image dimension ratio: 1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 21:9"
    )


class SeeDream4I2ISchema(BaseSchema):
    """Schema for SeeDream 4.0 Image-to-Image (seedream-4.0-i2i)"""

    model_id: str = Field(
        default="seedream-4.0-i2i",
        description="Model ID: seedream-4.0-i2i"
    )
    init_image: List[Any] = Field(
        ...,
        description="Array of image URLs (JPEG/PNG, up to 10 images)"
    )
    prompt: str = Field(
        ...,
        description="Text description of desired image transformation"
    )


class SeeDance10ProI2VSchema(BaseSchema):
    """Schema for SeeDance 1.0 Pro Image-to-Video (seedance-1.0-pro-i2v)"""

    model_id: str = Field(
        default="seedance-1.0-pro-i2v",
        description="Model ID: seedance-1.0-pro-i2v"
    )
    init_image: List[Any] = Field(
        ...,
        description="Image input array"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )


class OmniHumanSchema(BaseSchema):
    """Schema for Omni Human (omni-human)"""

    model_id: str = Field(
        default="omni-human",
        description="Model ID: omni-human"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    init_audio: Any = Field(
        ...,
        description="Reference audio file/URL (less than 30 sec)"
    )


class OmniHuman15Schema(BaseSchema):
    """Schema for Omni Human 1.5 (omni-human-1.5)"""

    model_id: str = Field(
        default="omni-human-1.5",
        description="Model ID: omni-human-1.5"
    )
    init_image: Any = Field(
        ...,
        description="Source image file/URL"
    )
    init_audio: Any = Field(
        ...,
        description="Audio file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description of desired video performance"
    )


class SeeDance10ProFastI2VSchema(BaseSchema):
    """Schema for SeeDance 1.0 Pro Fast Image-to-Video (seedance-1.0-pro-fast-i2v)"""

    model_id: str = Field(
        default="seedance-1.0-pro-fast-i2v",
        description="Model ID: seedance-1.0-pro-fast-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )


class SeeDance10ProFastT2VSchema(BaseSchema):
    """Schema for SeeDance 1.0 Pro Fast Text-to-Video (seedance-1.0-pro-fast-t2v)"""

    model_id: str = Field(
        default="seedance-1.0-pro-fast-t2v",
        description="Model ID: seedance-1.0-pro-fast-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
