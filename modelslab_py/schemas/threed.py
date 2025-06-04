from typing import Optional, List, Dict, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field

class Text23D(BaseSchema):
    prompt: str = Field(
        ...,
        description="Prompt for the 3D generation."
    )
    resolution: Optional[str] = Field(
        None,
        description="Resolution of the generated 3D model."
    )
    output_format: Optional[str] = Field(
        None,
        description="Output format of the generated 3D model."
    )
    render : Optional[bool] = Field(
        None,
        description="Whether to render the 3D model."
    )
    negative_prompt : Optional[str] = Field(
        None,
        description="Negative prompt for the 3D generation."
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
    ss_guidance_strength : Optional[float] = Field(
        None,
        description="Strength of style-space guidance for refinement."
    )
    slat_guidance_strength  : Optional[float] = Field(
        None,
        description="Strength of slat guidance for model details."
    )
    slat_sampling_steps : Optional[int] = Field(
        None,
        description="Number of steps for slat guidance sampling."
    )
    mesh_simplify : Optional[float] = Field(
        None,
        description="Mesh simplification factor."
    )
    foreground_ratio : Optional[float] = Field(
        None,
        description="Ratio of foreground in the generated model."
    )
    remove_bg  : Optional[bool] = Field(
        None,
        description="Whether to remove background from the generated model."
    )

    chunk_size : Optional[int] = Field(
        None,
        description="Chunk size for processing the model."
    )
    
    temp : Optional[str] = Field(
        None,
        description="Save output files in a temporary directory when set to `yes`."
    )

class Image23D(BaseSchema):
    image : Any = Field(
        ...,
        description="Initial image for the 3D generation."
    )
    resolution: Optional[int] = Field(
        None,
        description="Resolution of the generated 3D model."
    )
    output_format: Optional[str] = Field(
        None,
        description="Output format of the generated 3D model."
    )
    render : Optional[bool] = Field(
        None,
        description="Whether to render the 3D model."
    )
    
    seed : Optional[int] = Field(
        None,
        description="Seed for random number generation."
    )
    
    multi_image : Optional[bool] = Field(
        None,
        description="Whether to process multiple images."
    )
   
    ss_guidance_strength : Optional[float] = Field(
        None,
        description="Strength of style-space guidance for refinement."
    )

    slat_guidance_strength  : Optional[float] = Field(
        None,
        description="Strength of slat guidance for model details."
    )

    slat_sampling_steps : Optional[int] = Field(
        None,
        description="Number of steps for slat guidance sampling."
    )
    
    mesh_simplify : Optional[float] = Field(
        None,
        description="Mesh simplification factor."
    )
    
    chunk_size : Optional[int] = Field(
        None,
        description="Chunk size for processing the model."
    )
    
    temp : Optional[str] = Field(
        None,
        description="Save output files in a temporary directory when set to `yes`."
    )