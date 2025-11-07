from typing import Any, Optional
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class Gen4ImageSchema(BaseSchema):
    """Schema for Runway Gen4 Image Text-to-Image (gen4_image)"""

    model_id: str = Field(
        default="gen4_image",
        description="Model ID: gen4_image"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    aspect_ratio: str = Field(
        ...,
        description="Image aspect ratio (e.g., 16:9, 9:16, 1:1, 1920:1080)"
    )


class Gen4ImageTurboSchema(BaseSchema):
    """Schema for Runway Gen4 Image Turbo Image-to-Image (gen4_image_turbo)"""

    model_id: str = Field(
        default="gen4_image_turbo",
        description="Model ID: gen4_image_turbo"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    init_image: Any = Field(
        ...,
        description="Initial image URL or file upload"
    )
    init_image_2: Any = Field(
        ...,
        description="Second initial image URL or file upload"
    )


class Gen4AlephSchema(BaseSchema):
    """Schema for Runway Gen4 Aleph Video-to-Video (gen4_aleph)"""

    model_id: str = Field(
        default="gen4_aleph",
        description="Model ID: gen4_aleph"
    )
    init_video: Any = Field(
        ...,
        description="Reference video URL (MP4, webm, mov, Ogg, max 16MB)"
    )
    prompt: str = Field(
        ...,
        description="Description of desired video transformation (max 1000 characters)"
    )
    aspect_ratio: str = Field(
        ...,
        description="Video aspect ratio (1280:720, 720:1280, 1104:832, 960:960, 832:1104, 1584:672, 848:480)"
    )
    public_figure_threshold: Optional[str] = Field(
        None,
        description="Content moderation strictness (low, auto)"
    )
