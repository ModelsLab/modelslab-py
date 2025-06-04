from typing import Optional, List, Dict, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field

class Text2Video(BaseSchema):
    model_id : str = Field(
        ...,
        description="Model ID for the text-to-video generation."
    )
    prompt: str = Field(
        ...,
        description="Text prompt for the video generation."
    )

    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the video generation."
    )

    seed: Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )

    width: Optional[int] = Field(
        512,
        description="Width of the generated video."
    )

    height: Optional[int] = Field(
        512,
        description="Height of the generated video."
    )

    num_frames: Optional[int] = Field(
        30,
        description="Number of frames in the generated video."
    )

    num_inference_steps : Optional[int] = Field(
        50,
        description="Number of inference steps for the video generation."
    )

    guidance_scale : Optional[float] = Field(
        7.5,
        description="Guidance scale for the video generation."
    )

    fps : Optional[int] = Field(
        8,
        description="Frames per second for the generated video."
    )


class Image2Video(BaseSchema):
    model_id : str = Field(
        ...,
        description="Model ID for the text-to-video generation."
    )
    prompt: str = Field(
        ...,
        description="Text prompt for the video generation."
    )

    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the video generation."
    )

    seed: Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )

    width: Optional[int] = Field(
        512,
        description="Width of the generated video."
    )

    height: Optional[int] = Field(
        512,
        description="Height of the generated video."
    )

    num_frames: Optional[int] = Field(
        30,
        description="Number of frames in the generated video."
    )

    num_inference_steps : Optional[int] = Field(
        50,
        description="Number of inference steps for the video generation."
    )

    guidance_scale : Optional[float] = Field(
        7.5,
        description="Guidance scale for the video generation."
    )

    fps : Optional[int] = Field(
        8,
        description="Frames per second for the generated video."
    )

    init_image : Optional[Any] = Field(
        None,
        description="Initial image for the video generation."
    )

class Text2VideoUltra(BaseSchema):
    
    prompt: str = Field(
        ...,
        description="Text prompt for the video generation."
    )

    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the video generation."
    )

    seed: Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )

    resolution: Optional[str] = Field(
        "512x512",
        description="Resolution of the generated video."
    )

    num_frames: Optional[int] = Field(
        30,
        description="Number of frames in the generated video."
    )

    num_inference_steps : Optional[int] = Field(
        50,
        description="Number of inference steps for the video generation."
    )

    guidance_scale : Optional[float] = Field(
        7.5,
        description="Guidance scale for the video generation."
    )

    fps : Optional[int] = Field(
        8,
        description="Frames per second for the generated video."
    )
    portrait: Optional[bool] = Field(
        None,
        description="Whether to generate a portrait video."
    )
    sample_shift: Optional[int] = Field(
        None,
        description="Whether to apply sample shift."
    )
