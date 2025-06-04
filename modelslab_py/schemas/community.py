from typing import Optional, List, Dict, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field

class Text2Image(BaseSchema):
    """
    Schema for text-to-image generation.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for image generation."
    )
    model_id : Optional[str] = Field(
        None,
        description="Model ID for the image generation."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for image generation."
    )
    width: Optional[int] = Field(
        None,
        description="Width of the generated image."
    )
    height: Optional[int] = Field(
        None,
        description="Height of the generated image."
    )
    samples: Optional[int] = Field(
        None,
        description="Number of samples to generate."
    )
    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of inference steps for image generation."
    )
    safety_checker: Optional[str] = Field(
        None,
        description="Whether to use a safety checker."
    )
    seed: Optional[int] = Field(
        None,
        description="Random seed for image generation."
    )
    enhance_prompt: Optional[str] = Field(
        None,
        description="Whether to enhance the prompt."
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Guidance scale for image generation."
    )
    multi_lingual: Optional[str] = Field(
        None,
        description="Whether to use multi-lingual support."
    )
    panorama: Optional[str] = Field(
        None,
        description="Whether to generate a panorama."
    )
    self_attention: Optional[str] = Field(
        None,
        description="Whether to use self-attention."
    )
    upscale: Optional[str] = Field(
        None,
        description="Whether to upscale the image."
    )
    lora_model: Optional[str] = Field(
        None,
        description="Lora model for image generation."
    )
    lora_strength: Optional[float] = Field(
        None,
        description="Strength of the lora model."
    )
    scheduler   : Optional[str] = Field(
        None,
        description="Scheduler for image generation."
    )
    clip_skip	: Optional[int] = Field(
        None,
        description="Whether to use clip skip."
    )


class Image2Image(BaseSchema):
    """
    Schema for image-2-image generation.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for image generation."
    )
    model_id : Optional[str] = Field(
        None,
        description="Model ID for the image generation."
    )
    init_image: Optional[Any] = Field(
        None,
        description="Initial image for the image generation."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for image generation."
    )
    width: Optional[int] = Field(
        None,
        description="Width of the generated image."
    )
    height: Optional[int] = Field(
        None,
        description="Height of the generated image."
    )
    samples: Optional[int] = Field(
        None,
        description="Number of samples to generate."
    )
    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of inference steps for image generation."
    )
    safety_checker: Optional[str] = Field(
        None,
        description="Whether to use a safety checker."
    )
    seed: Optional[int] = Field(
        None,
        description="Random seed for image generation."
    )
    enhance_prompt: Optional[str] = Field(
        None,
        description="Whether to enhance the prompt."
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Guidance scale for image generation."
    )
    multi_lingual: Optional[str] = Field(
        None,
        description="Whether to use multi-lingual support."
    )
    panorama: Optional[str] = Field(
        None,
        description="Whether to generate a panorama."
    )
    self_attention: Optional[str] = Field(
        None,
        description="Whether to use self-attention."
    )
    upscale: Optional[str] = Field(
        None,
        description="Whether to upscale the image."
    )
    lora_model: Optional[str] = Field(
        None,
        description="Lora model for image generation."
    )
    lora_strength: Optional[float] = Field(
        None,
        description="Strength of the lora model."
    )
    scheduler   : Optional[str] = Field(
        None,
        description="Scheduler for image generation."
    )
    clip_skip	: Optional[int] = Field(
        None,
        description="Whether to use clip skip."
    )

class Inpainting(BaseSchema):
    """
    Schema for text-to-image generation.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for image generation."
    )
    model_id : Optional[str] = Field(
        None,
        description="Model ID for the image generation."
    )
    init_image: Optional[Any] = Field(
        None,
        description="Initial image for the image generation."
    )
    mask_image: Optional[Any] = Field(
        None,
        description="Mask image for the inpainting."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for image generation."
    )
    width: Optional[int] = Field(
        None,
        description="Width of the generated image."
    )
    height: Optional[int] = Field(
        None,
        description="Height of the generated image."
    )
    samples: Optional[int] = Field(
        None,
        description="Number of samples to generate."
    )
    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of inference steps for image generation."
    )
    safety_checker: Optional[str] = Field(
        None,
        description="Whether to use a safety checker."
    )
    seed: Optional[int] = Field(
        None,
        description="Random seed for image generation."
    )
    enhance_prompt: Optional[str] = Field(
        None,
        description="Whether to enhance the prompt."
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Guidance scale for image generation."
    )
    multi_lingual: Optional[str] = Field(
        None,
        description="Whether to use multi-lingual support."
    )
    panorama: Optional[str] = Field(
        None,
        description="Whether to generate a panorama."
    )
    self_attention: Optional[str] = Field(
        None,
        description="Whether to use self-attention."
    )
    upscale: Optional[str] = Field(
        None,
        description="Whether to upscale the image."
    )
    lora_model: Optional[str] = Field(
        None,
        description="Lora model for image generation."
    )
    lora_strength: Optional[float] = Field(
        None,
        description="Strength of the lora model."
    )
    scheduler   : Optional[str] = Field(
        None,
        description="Scheduler for image generation."
    )
    clip_skip	: Optional[int] = Field(
        None,
        description="Whether to use clip skip."
    )

class ControlNet(BaseSchema):
    prompt: str = Field(
        ...,
        description="Text prompt for image generation."
    )
    model_id : Optional[str] = Field(
        None,
        description="Model ID for the image generation."
    )
    init_image: Optional[Any] = Field(
        None,
        description="Initial image for the image generation."
    )
    mask_image: Optional[Any] = Field(
        None,
        description="Mask image for the inpainting."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for image generation."
    )
    width: Optional[int] = Field(
        None,
        description="Width of the generated image."
    )
    height: Optional[int] = Field(
        None,
        description="Height of the generated image."
    )
    samples: Optional[int] = Field(
        None,
        description="Number of samples to generate."
    )
    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of inference steps for image generation."
    )
    safety_checker: Optional[str] = Field(
        None,
        description="Whether to use a safety checker."
    )
    seed: Optional[int] = Field(
        None,
        description="Random seed for image generation."
    )
    enhance_prompt: Optional[str] = Field(
        None,
        description="Whether to enhance the prompt."
    )
    guidance_scale: Optional[float] = Field(
        None,
        description="Guidance scale for image generation."
    )
    multi_lingual: Optional[str] = Field(
        None,
        description="Whether to use multi-lingual support."
    )
    panorama: Optional[str] = Field(
        None,
        description="Whether to generate a panorama."
    )
    self_attention: Optional[str] = Field(
        None,
        description="Whether to use self-attention."
    )
    upscale: Optional[str] = Field(
        None,
        description="Whether to upscale the image."
    )
    lora_model: Optional[str] = Field(
        None,
        description="Lora model for image generation."
    )
    lora_strength: Optional[float] = Field(
        None,
        description="Strength of the lora model."
    )
    scheduler   : Optional[str] = Field(
        None,
        description="Scheduler for image generation."
    )
    clip_skip	: Optional[int] = Field(
        None,
        description="Whether to use clip skip."
    )
    controlnet_model: Optional[str] = Field(
        None,
        description="ControlNet model for image generation."
    )
    controlnet_type: Optional[str] = Field(
        None,
        description="ControlNet type for image generation."
    )
    strength: Optional[float] = Field(
        None,
        description="Strength of the ControlNet model."
    )