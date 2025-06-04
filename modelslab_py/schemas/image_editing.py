from typing import Optional, List, Dict, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field

class OutpaintingSchema(BaseSchema):
    """
    Schema for outpainting.
    """
    prompt: str = Field(
        ...,
        description="Prompt for the outpainting."
    )
    image: Any = Field(
        ...,
        description="Image for the outpainting."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the outpainting."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    overlap_width: Optional[int] = Field(
        64,
        description="Width of the overlap area."
    )
    num_inference_steps: Optional[int] = Field(
        20,
        description="Number of inference steps."
    )
    guidance_scale: Optional[float] = Field(
        7.5,
        description="Guidance scale for the outpainting."
    )
    seed: Optional[int] = Field(
        None,
        description="Seed for the outpainting."
    )

class BlipDiffusionSchema(BaseSchema):
    """
    Schema for BLIP diffusion.
    """
    prompt: str = Field(
        ...,
        description="Prompt for the BLIP diffusion."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the BLIP diffusion."
    )
    task: Optional[str] = Field(
        "text_to_image",
        description="Task for the BLIP diffusion."
    )
    condition_image: Optional[Any] = Field(
        None,
        description="Condition image for the BLIP diffusion."
    )
    condition_subject : Optional[str] = Field(
        None,
        description="Condition subject for the BLIP diffusion."
    )
    target_subject : Optional[str] = Field(
        None,
        description="Target subject for the BLIP diffusion."
    )
    style_subject   : Optional[str] = Field(
        None,
        description="Style subject for the BLIP diffusion."
    )

    controlnet_condition_image  : Optional[Any] = Field(
        None,
        description="ControlNet condition image for the BLIP diffusion."
    )

    width : Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height : Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    guidance_scale : Optional[float] = Field(
        7.5,
        description="Guidance scale for the BLIP diffusion."
    )

class MagicMixSchema(BaseSchema):
    """
    Schema for Magic Mix.
    """
    prompt: str = Field(
        ...,
        description="Prompt for the Magic Mix."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the Magic Mix."
    )
    image: Any = Field(
        ...,
        description="Image for the Magic Mix."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    steps: Optional[int] = Field(
        20,
        description="Number of inference steps."
    )
    guidance_scale: Optional[float] = Field(
        7.5,
        description="Guidance scale for the Magic Mix."
    )
    seed: Optional[int] = Field(
        None,
        description="Seed for the Magic Mix."
    )
    kmax: Optional[float] = Field(
        0.5,
        description="Kmax for the Magic Mix."
    )
    kmin : Optional[float] = Field(
        0.5,
        description="Kmin for the Magic Mix."
    )
    mix_factor : Optional[float] = Field(
        0.5,
        description="Mix factor for the Magic Mix."
    )
    samples : Optional[int] = Field(
        1,
        description="Number of samples for the Magic Mix."
    )

class BackgroundRemoverSchema(BaseSchema):
    """
    Schema for background remover.
    """
    image: Any = Field(
        ...,
        description="Image for the background remover."
    )
    alpha_matting : Optional[bool] = Field(
        False,
        description="Whether to use alpha matting."
    )
    post_process_mask : Optional[bool] = Field(
        False,
        description="Whether to post-process the mask."
    )
    only_mask : Optional[bool] = Field(
        False,
        description="Whether to return only the mask."
    )
    inverse_mask : Optional[bool] = Field(
        False,
        description="Whether to return the inverse mask."
    )
    seed : Optional[int] = Field(
        None,
        description="Seed for the background remover."
    )
    base64 : Optional[bool] = Field(
        False,
        description="Whether to return the image as base64."
    )
    alpha_matting_foreground_threshold : Optional[int] = Field(
        240,
        description="Foreground threshold for alpha matting."
    )

    alpha_matting_background_threshold : Optional[int] = Field(
        20,
        description="Background threshold for alpha matting."
    )
    alpha_matting_erode_size : Optional[int] = Field(
        5,
        description="Erode size for alpha matting."
    )


class SuperResolutionSchema(BaseSchema):
    """
    Schema for super resolution.
    """
    init_image: Any = Field(
        ...,
        description="Initial image for the super resolution."
    )
    model_id : Optional[str] = Field(
        "ultra_resolution",
        description="Model ID for the super resolution."
    )
    scale : Optional[int] = Field(
        4,
        description="Scale for the super resolution."
    )
    face_enhance : Optional[bool] = Field(
        False,
        description="Whether to enhance the face."
    )

class FashionSchema(BaseSchema):
    """
    Schema for fashion.
    """
    init_image: Any = Field(
        ...,
        description="Initial image for the fashion."
    )
    prompt: Optional[str] = Field(
        None,
        description="Prompt for the fashion."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the fashion."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    num_inference_steps: Optional[int] = Field(
        20,
        description="Number of inference steps."
    )
    cloth_image: Optional[Any] = Field(
        None,
        description="Cloth image for the fashion."
    )
    cloth_type: Optional[str] = Field(
        "dress",
        description="Type of cloth for the fashion."
    )

class ObjectRemovalSchema(BaseSchema):
    """
    Schema for object removal.
    """
    init_image: Any = Field(
        ...,
        description="Initial image for the object removal."
    )
    mask_image: Any = Field(
        ...,
        description="Mask image for the object removal."
    )
    
class FacegenSchema(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the face generation."
    )
    face_image: Optional[Any] = Field(
        None,
        description="Face image for the face generation."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    num_inference_steps: Optional[int] = Field(
        20,
        description="Number of inference steps."
    )
    guidance_scale: Optional[float] = Field(
        7.5,
        description="Guidance scale for the face generation."
    )
    s_scale: Optional[float] = Field(
        7.5,
        description="S scale for the face generation."
    )
    samples: Optional[int] = Field(
        1,
        description="Number of samples for the face generation."
    )
    safety_checker: Optional[bool] = Field(
        True,   
        description="Whether to use safety checker."
    )
    safety_checker_type: Optional[str] = Field(
        "black",
        description="Type of safety checker."
    )
    base64: Optional[bool] = Field(
        False,
        description="Whether to return the image as base64."
    )
    style: Optional[str] = Field(
        "realistic",
        description="Style of the face generation."
    )

class InpaintingSchema(BaseSchema):
    """
    Schema for inpainting.
    """
    prompt: str = Field(
        ...,
        description="Prompt for the inpainting."
    )
    init_image: Any = Field(
        ...,
        description="Image for the inpainting."
    )
    mask_image: Any = Field(
        ...,
        description="Mask image for the inpainting."
    )
    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the inpainting."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    num_inference_steps: Optional[int] = Field(
        20,
        description="Number of inference steps."
    )
    guidance_scale: Optional[float] = Field(
        7.5,
        description="Guidance scale for the inpainting."
    )
    seed: Optional[int] = Field(
        None,
        description="Seed for the inpainting."
    )
    samples: Optional[int] = Field(
        1,
        description="Number of samples for the inpainting."
    )
    base64: Optional[bool] = Field(
        False,
        description="Whether to return the image as base64."
    )

class HeadshotSchema(BaseSchema):
    """
    Schema for headshot generation.
    """
    prompt: str = Field(
        ...,
        description="Prompt for the face generation."
    )
    face_image: Optional[Any] = Field(
        None,
        description="Face image for the face generation."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    num_inference_steps: Optional[int] = Field(
        20,
        description="Number of inference steps."
    )
    guidance_scale: Optional[float] = Field(
        7.5,
        description="Guidance scale for the face generation."
    )
    s_scale: Optional[float] = Field(
        7.5,
        description="S scale for the face generation."
    )
    samples: Optional[int] = Field(
        1,
        description="Number of samples for the face generation."
    )
    safety_checker: Optional[bool] = Field(
        True,   
        description="Whether to use safety checker."
    )
    safety_checker_type: Optional[str] = Field(
        "black",
        description="Type of safety checker."
    )
    base64: Optional[bool] = Field(
        False,
        description="Whether to return the image as base64."
    )
    style: Optional[str] = Field(
        "realistic",
        description="Style of the face generation."
    )


class FluxHeadshotSchema(BaseSchema):
    """
    Schema for headshot generation.
    """
    prompt: str = Field(
        ...,
        description="Prompt for the face generation."
    )
    face_image: Optional[Any] = Field(
        None,
        description="Face image for the face generation."
    )
    width: Optional[int] = Field(
        512,
        description="Width of the output image."
    )
    height: Optional[int] = Field(
        512,
        description="Height of the output image."
    )
    num_inference_steps: Optional[int] = Field(
        20,
        description="Number of inference steps."
    )
    guidance_scale: Optional[float] = Field(
        7.5,
        description="Guidance scale for the face generation."
    )
    s_scale: Optional[float] = Field(
        7.5,
        description="S scale for the face generation."
    )
    samples: Optional[int] = Field(
        1,
        description="Number of samples for the face generation."
    )
    safety_checker: Optional[bool] = Field(
        True,   
        description="Whether to use safety checker."
    )
    safety_checker_type: Optional[str] = Field(
        "black",
        description="Type of safety checker."
    )
    base64: Optional[bool] = Field(
        False,
        description="Whether to return the image as base64."
    )
    style: Optional[str] = Field(
        "realistic",
        description="Style of the face generation."
    )