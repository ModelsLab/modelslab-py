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