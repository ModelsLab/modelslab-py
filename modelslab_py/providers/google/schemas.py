from typing import Optional, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class Imagen4Schema(BaseSchema):
    """Schema for Google Imagen 4 Text-to-Image (imagen-4)"""

    model_id: str = Field(
        default="imagen-4",
        description="Model ID: imagen-4"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    aspect_ratio: str = Field(
        ...,
        description="Image aspect ratio (1:1, 3:4, 4:3, 9:16, 16:9)"
    )


class Imagen3Schema(BaseSchema):
    """Schema for Google Imagen 3 Text-to-Image (imagen-3)"""

    model_id: str = Field(
        default="imagen-3",
        description="Model ID: imagen-3"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )


class Imagen40FastGenerateSchema(BaseSchema):
    """Schema for Google Imagen 4.0 Fast Generate Text-to-Image (imagen-4.0-fast-generate)"""

    model_id: str = Field(
        default="imagen-4.0-fast-generate",
        description="Model ID: imagen-4.0-fast-generate"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation (max 480 tokens)"
    )
    aspect_ratio: str = Field(
        ...,
        description="Image aspect ratio (1:1, 3:4, 4:3, 9:16, 16:9)"
    )


class Imagen40UltraSchema(BaseSchema):
    """Schema for Google Imagen 4.0 Ultra Text-to-Image (imagen-4.0-ultra)"""

    model_id: str = Field(
        default="imagen-4.0-ultra",
        description="Model ID: imagen-4.0-ultra"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation (max 480 tokens)"
    )
    aspect_ratio: str = Field(
        ...,
        description="Image aspect ratio (1:1, 3:4, 4:3, 9:16, 16:9)"
    )
    samples: Optional[int] = Field(
        None,
        description="Number of images to generate (1-4)"
    )


class NanoBananaT2ISchema(BaseSchema):
    """Schema for Google Nano Banana Text-to-Image (nano-banana-t2i)"""

    model_id: str = Field(
        default="nano-banana-t2i",
        description="Model ID: nano-banana-t2i"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )


class NanoBananaSchema(BaseSchema):
    """Schema for Google Nano Banana Image-to-Image (nano-banana)"""

    model_id: str = Field(
        default="nano-banana",
        description="Model ID: nano-banana"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    init_image: Any = Field(
        ...,
        description="URL or file of first input image"
    )
    init_image_2: Any = Field(
        ...,
        description="URL or file of second input image"
    )
