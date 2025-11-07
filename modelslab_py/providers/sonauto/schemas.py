from typing import Optional, Any, List
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class SonautoSongSchema(BaseSchema):
    """Schema for Sonauto Song Generation (sonauto_song)"""

    model_id: str = Field(
        default="sonauto_song",
        description="Model ID: sonauto_song"
    )
    prompt: str = Field(
        ...,
        description="Descriptive text for generating audio"
    )


class SongExtenderSchema(BaseSchema):
    """Schema for Sonauto Song Extender (song-extender)"""

    model_id: str = Field(
        default="song-extender",
        description="Model ID: song-extender"
    )
    init_audio: Any = Field(
        ...,
        description="Initial audio file or URL"
    )
    prompt: str = Field(
        ...,
        description="Text instruction for song extension"
    )
    extend_duration: float = Field(
        ...,
        description="Extension length (0-85.0 seconds)"
    )
    side: Optional[str] = Field(
        None,
        description="Extension direction (right or left)"
    )


class SongInpaintSchema(BaseSchema):
    """Schema for Sonauto Song Inpaint (song-inpaint)"""

    model_id: str = Field(
        default="song-inpaint",
        description="Model ID: song-inpaint"
    )
    lyrics: str = Field(
        ...,
        description="Lyrics"
    )
    init_audio: Any = Field(
        ...,
        description="Init audio (URL or file)"
    )
    sections: List[Any] = Field(
        ...,
        description="Audio timestamp where you want to apply inpainting"
    )
