from typing import Optional, List, Dict, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field

class RealtimeText2ImageSchema(BaseSchema):
    """
    Schema for real-time text-to-image generation.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for image generation."
    )
    init_image: Optional[Any] = Field(
        None,
        description="Initial image for the generation."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the image generation."
    )
    strength: Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64: Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed: Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of inference steps."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the generated image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the generated image."
    )
    samples: Optional[int] = Field(
        1,
        description="Number of images to generate per prompt."
    )


class RealtimeImage2ImageSchema(BaseSchema):

    """
    Schema for real-time image-to-image generation.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for image generation."
    )
    init_image: Any = Field(
        None,
        description="Initial image for the generation."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the image generation."
    )
    strength: Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64: Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed: Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of inference steps."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the generated image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the generated image."
    )
    samples: Optional[int] = Field(
        1,
        description="Number of images to generate per prompt."
    )

class RealtimeInpaintingSchema(BaseSchema):
    """
    Schema for real-time inpainting generation.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for image generation."
    )
    init_image: Any = Field(
        None,
        description="Initial image for the generation."
    )
    mask_image: Any = Field(
        None,
        description="Mask image for the inpainting generation."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the image generation."
    )
    strength: Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64: Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed: Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of inference steps."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the generated image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the generated image."
    )
    samples: Optional[int] = Field(
        1,
        description="Number of images to generate per prompt."
    )