from typing import Optional, List, Dict, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field

class SkechRendringSchema(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the interior generation."
    )
    init_image : Any = Field(
        None,
        description="Initial image for the interior generation."
    )
    negative_prompt : Optional[str] = Field(
        None,
        description="Negative prompt for the interior generation."
    )

    strength : Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64 : Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed : Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale : Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps : Optional[int] = Field(
        None,
        description="Number of inference steps."
    )

class InteriorSchema(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the interior generation."
    )
    init_image : Any = Field(
        None,
        description="Initial image for the interior generation."
    )
    negative_prompt : Optional[str] = Field(
        None,
        description="Negative prompt for the interior generation."
    )

    strength : Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64 : Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed : Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale : Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps : Optional[int] = Field(
        None,
        description="Number of inference steps."
    )

class RoomDecoratorSchema(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the interior generation."
    )
    init_image : Any = Field(
        None,
        description="Initial image for the interior generation."
    )
    negative_prompt : Optional[str] = Field(
        None,
        description="Negative prompt for the interior generation."
    )

    strength : Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64 : Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed : Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale : Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps : Optional[int] = Field(
        None,
        description="Number of inference steps."
    )

class FloorSchema(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the interior generation."
    )
    init_image : Any = Field(
        None,
        description="Initial image for the interior generation."
    )
    negative_prompt : Optional[str] = Field(
        None,
        description="Negative prompt for the interior generation."
    )

    strength : Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64 : Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed : Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale : Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps : Optional[int] = Field(
        None,
        description="Number of inference steps."
    )

class ExteriorSchema(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the interior generation."
    )
    init_image : Any = Field(
        None,
        description="Initial image for the interior generation."
    )
    negative_prompt : Optional[str] = Field(
        None,
        description="Negative prompt for the interior generation."
    )

    strength : Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64 : Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed : Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale : Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps : Optional[int] = Field(
        None,
        description="Number of inference steps."
    )

class ScenarioSchema(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the interior generation."
    )
    init_image : Any = Field(
        None,
        description="Initial image for the interior generation."
    )
    negative_prompt : Optional[str] = Field(
        None,
        description="Negative prompt for the interior generation."
    )

    strength : Optional[float] = Field(
        None,
        description="Strength of the initial image influence."
    )
    base64 : Optional[bool] = Field(
        None,
        description="Whether to return the image as base64."
    )
    seed : Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    guidance_scale : Optional[float] = Field(
        None,
        description="Guidance scale for the generation."
    )
    num_inference_steps : Optional[int] = Field(
        None,
        description="Number of inference steps."
    )
    scenario : str = Field(
        None,
        description="Scenario for the generation."
    )

class ObjectRemovalSchema(BaseSchema):
    """
    Schema for object removal from images.
    """
    init_image: str = Field(
        ...,
        description="Image from which object will be removed."
    )
    object_name: str = Field(
        ...,
        description="Object name on the image that needs to be removed."
    )
    base64: Optional[bool] = Field(
        False,
        description="Whether to return the image as base64."
    )

class InteriorMixerSchema(BaseSchema):
    """
    Schema for interior mixer.
    """
    init_image: str = Field(
        ...,
        description="Room image in which object wants to be added."
    )
    object_image: str = Field(
        ...,
        description="Object which we want to add."
    )
    prompt: str = Field(
        ...,
        description="Prompt required for generation."
    )
    width: Optional[int] = Field(
        None,
        description="Width of output image. Min: 512, Max: 2048. If not provided, uses original image resolution."
    )
    height: Optional[int] = Field(
        None,
        description="Height of the output image. Min: 512, Max: 2048. If not provided, uses original image resolution."
    )
    guidance_scale: Optional[int] = Field(
        None,
        description="The scale for classifier-free guidance."
    )
    num_inference_steps: Optional[int] = Field(
        8,
        description="Number of inference steps required for generation."
    )
    base64: Optional[bool] = Field(
        False,
        description="Whether to return the image as base64."
    )