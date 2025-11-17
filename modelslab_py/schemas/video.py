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

    resolution: Optional[int] = Field(
        None,
        description="Resolution of the generated output. Maximum is 480."
    )

    num_frames: Optional[int] = Field(
        None,
        description="Number of frames in the generated video."
    )

    num_inference_steps: Optional[int] = Field(
        None,
        description="Number of denoising steps. Maximum is 8."
    )

    guidance_scale: Optional[float] = Field(
        None,
        description="Scale for classifier-free guidance. Minimum is 1.0, maximum is 2.0."
    )

    fps: Optional[int] = Field(
        None,
        description="Frames per second for the generated video. Must be less than num_frames. Maximum is 18."
    )

    portrait: Optional[bool] = Field(
        None,
        description="Whether to generate a portrait video."
    )

    sample_shift: Optional[int] = Field(
        None,
        description="Controls the sampling shift in the generation process."
    )

    temp: Optional[bool] = Field(
        None,
        description="If true, stores the video in temporary storage (cleaned every 24 hours)."
    )

    webhook: Optional[str] = Field(
        None,
        description="A URL to receive a POST API call once the video generation is complete."
    )

    track_id: Optional[str] = Field(
        None,
        description="Unique ID for webhook tracking."
    )

class Image2VideoUltra(BaseSchema):

    prompt: str = Field(
        ...,
        description="Text prompt for the video generation."
    )

    init_image: str = Field(
        ...,
        description="Link to a valid PNG, JPEG, or other image format file to use as initial image conditioning."
    )

    negative_prompt: Optional[str] = Field(
        None,
        description="Negative prompt for the video generation."
    )

    seed: Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )

    resolution: Optional[int] = Field(
        320,
        description="Resolution of the generated output. Maximum is 480."
    )

    num_frames: Optional[int] = Field(
        92,
        description="Number of frames in the generated video."
    )

    num_inference_steps: Optional[int] = Field(
        8,
        description="Number of denoising steps. Maximum is 8."
    )

    guidance_scale: Optional[float] = Field(
        1.0,
        description="Scale for classifier-free guidance. Min is 1.0, Max is 2.0."
    )

    fps: Optional[int] = Field(
        None,
        description="Frames per second for the generated video. Should be less than num_frames. Maximum is 18."
    )

    portrait: Optional[bool] = Field(
        False,
        description="Whether to generate a portrait video."
    )

    sample_shift: Optional[int] = Field(
        3,
        description="Controls the sampling shift in the generation process."
    )

    temp: Optional[bool] = Field(
        False,
        description="If true, stores the video in temporary storage (cleaned every 24 hours)."
    )

    webhook: Optional[str] = Field(
        None,
        description="A URL to receive a POST API call once the video generation is complete."
    )

    track_id: Optional[str] = Field(
        None,
        description="Unique ID for webhook tracking."
    )

class WatermarkRemoverSchema(BaseSchema):
    """
    Schema for watermark removal from videos.
    """
    init_video: str = Field(
        ...,
        description="URL of the initial video with watermark."
    )
