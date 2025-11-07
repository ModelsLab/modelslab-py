from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class InworldTts1Schema(BaseSchema):
    """Schema for Inworld TTS 1 Text-to-Speech (inworld-tts-1)"""

    model_id: str = Field(
        default="inworld-tts-1",
        description="Model ID: inworld-tts-1"
    )
    prompt: str = Field(
        ...,
        description="Text to convert to speech"
    )
    voice_id: str = Field(
        ...,
        description="Voice selection (e.g., Alex, Ashley, Craig)"
    )
