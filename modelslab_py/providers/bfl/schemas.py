from typing import Optional, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class FluxPro1752000026Schema(BaseSchema):
    """Schema for FLUX.1 - Pro (flux-pro-1752000026)"""

    model_id: str = Field(
        default="flux-pro-1752000026",
        description="Model ID: flux-pro-1752000026"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    lora_model: Optional[str] = Field(
        None,
        description="Multiple model selection"
    )
    width: int = Field(
        ...,
        description="Image width (512-1024 pixels)"
    )
    height: int = Field(
        ...,
        description="Image height (512-1024 pixels)"
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Elements to avoid in the generated image"
    )
    scheduler: Optional[str] = Field(
        None,
        description="Image generation scheduler: DPM++ 2M, DPM++ SDE, Euler, Euler a"
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Creativity scale (1-10)"
    )


class FluxPro11Schema(BaseSchema):
    """Schema for Flux Pro 1.1 (flux-pro-1.1)"""

    model_id: str = Field(
        default="flux-pro-1.1",
        description="Model ID: flux-pro-1.1"
    )
    prompt: str = Field(
        ...,
        description="Text description for image generation"
    )
    lora_model: Optional[str] = Field(
        None,
        description="Multiple model selection"
    )
    width: int = Field(
        ...,
        description="Image width (512-1024 pixels)"
    )
    height: int = Field(
        ...,
        description="Image height (512-1024 pixels)"
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Elements to avoid in the generated image"
    )
    scheduler: Optional[str] = Field(
        None,
        description="Image generation scheduler: DPM++ 2M, DPM++ SDE, Euler, Euler a"
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Creativity scale (1-10)"
    )


class FluxPro11UltraSchema(BaseSchema):
    """Schema for Flux Pro 1.1 Ultra (flux-pro-1.1-ultra)"""

    model_id: str = Field(
        default="flux-pro-1.1-ultra",
        description="Model ID: flux-pro-1.1-ultra"
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
    negative_prompt: Optional[str] = Field(
        None,
        description="Elements to avoid in the generated image"
    )
    scheduler: Optional[str] = Field(
        None,
        description="Image generation scheduler: DPM++ 2M, DPM++ SDE, Euler, Euler a"
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Creativity scale (1-10)"
    )


class FluxKontextProSchema(BaseSchema):
    """Schema for Flux Kontext Pro (flux-kontext-pro)"""

    model_id: str = Field(
        default="flux-kontext-pro",
        description="Model ID: flux-kontext-pro"
    )
    init_image: Any = Field(
        ...,
        description="Reference image file/URL to edit"
    )
    prompt: str = Field(
        ...,
        description="Description of desired image changes"
    )
    aspect_ratio: Optional[str] = Field(
        None,
        description="Image dimension options: 21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16, 9:21"
    )


class Flux2ProSchema(BaseSchema):
    """Schema for Flux 2 Pro (flux-2-pro)"""

    model_id: str = Field(
        default="flux-2-pro",
        description="Model ID: flux-2-pro"
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


class Flux2ProImageEditingSchema(BaseSchema):
    """Schema for Flux 2 Pro Image Editing (flux-2-pro)"""

    model_id: str = Field(
        default="flux-2-pro",
        description="Model ID: flux-2-pro"
    )
    init_image: Any = Field(
        ...,
        description="Reference image URLs in JPEG, PNG format. Can add up to 10 images"
    )
    prompt: str = Field(
        ...,
        description="Text prompt for the type of image you want to generate"
    )
