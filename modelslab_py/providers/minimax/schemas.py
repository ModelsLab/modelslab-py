from typing import Optional, List, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class Hailuo23T2VSchema(BaseSchema):
    """Schema for Hailuo 2.3 Text-to-Video (Hailuo-2.3-t2v)"""

    model_id: str = Field(
        default="Hailuo-2.3-t2v",
        description="Model ID: Hailuo-2.3-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )


class Hailuo02T2VSchema(BaseSchema):
    """Schema for Hailuo 02 Text-to-Video (Hailuo-02-t2v)"""

    model_id: str = Field(
        default="Hailuo-02-t2v",
        description="Model ID: Hailuo-02-t2v"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )


class Hailuo23I2VSchema(BaseSchema):
    """Schema for Hailuo 2.3 Image-to-Video (Hailuo-2.3-i2v)"""

    model_id: str = Field(
        default="Hailuo-2.3-i2v",
        description="Model ID: Hailuo-2.3-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: Optional[str] = Field(
        None,
        description="Video duration: 6s or 10s (default 6s)"
    )


class Hailuo23FastI2VSchema(BaseSchema):
    """Schema for Hailuo 2.3 Fast Image-to-Video (Hailuo-2.3-Fast-i2v)"""

    model_id: str = Field(
        default="Hailuo-2.3-Fast-i2v",
        description="Model ID: Hailuo-2.3-Fast-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
    duration: Optional[str] = Field(
        None,
        description="Video duration: 6s or 10s"
    )


class Hailuo02I2VSchema(BaseSchema):
    """Schema for Hailuo 02 Image-to-Video (Hailuo-02-i2v)"""

    model_id: str = Field(
        default="Hailuo-02-i2v",
        description="Model ID: Hailuo-02-i2v"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )


class Hailuo02StartEndFrameSchema(BaseSchema):
    """Schema for Hailuo 02 Start-End Frame (Hailuo-02-start-end-frame)"""

    model_id: str = Field(
        default="Hailuo-02-start-end-frame",
        description="Model ID: Hailuo-02-start-end-frame"
    )
    init_image: List[Any] = Field(
        ...,
        description="Array of reference images for start and end frames"
    )
    prompt: str = Field(
        ...,
        description="Text description for video generation"
    )
