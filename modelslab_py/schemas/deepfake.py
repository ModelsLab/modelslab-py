from typing import Optional, List, Dict, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field

class SpecificFaceSwap(BaseSchema):
    """
    Schema for specific face swap.
    """
    init_image: Any = Field(
        ...,
        description="Initial image for the face swap."
    )
    target_image: Any = Field(
        ...,
        description="Target image for the face swap."
    )
    reference_image : Any = Field(
        ...,
        description="Reference image for the face swap."
    )
    watermark: Optional[bool] = Field(
        None,
        description="Whether to add a watermark to the output."
    )

class MultipleFaceSwap(BaseSchema):
    """
    Schema for specific face swap.
    """
    init_image: Any = Field(
        ...,
        description="Initial image for the face swap."
    )
    target_image: Any = Field(
        ...,
        description="Target image for the face swap."
    )
    watermark: Optional[bool] = Field(
        None,
        description="Whether to add a watermark to the output."
    )

class SingleVideoSwap(BaseSchema):
    init_image: Any = Field(
        ...,
        description="Initial image for the face swap."
    )

    init_video : Any = Field(   
        ...,
        description="Initial video for the face swap."
    )
    output_format : Optional[str] = Field(
        "mp4",
        description="Output format of the generated video."
    )

    watermark: Optional[bool] = Field(
        None,
        description="Whether to add a watermark to the output."
    )

class SpecificVideoSwap(BaseSchema):
    init_image: Any = Field(
        ...,
        description="Initial image for the face swap."
    )

    init_video : Any = Field(   
        ...,
        description="Initial video for the face swap."
    )
    reference_image : Any = Field(
        ...,
        description="Reference image for the face swap."
    )
    output_format : Optional[str] = Field(
        "mp4",
        description="Output format of the generated video."
    )

    watermark: Optional[bool] = Field(
        None,
        description="Whether to add a watermark to the output."
    )