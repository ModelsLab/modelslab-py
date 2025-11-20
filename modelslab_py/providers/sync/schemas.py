from typing import Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class Lipsync2Schema(BaseSchema):
    """Schema for Lipsync 2 (lipsync-2)"""

    model_id: str = Field(
        default="lipsync-2",
        description="Model ID: lipsync-2"
    )
    init_video: Any = Field(
        ...,
        description="Reference video file/URL"
    )
    init_audio: Any = Field(
        ...,
        description="Reference audio file/URL"
    )
