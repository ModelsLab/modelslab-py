from typing import Optional, Any
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class ScribeV1Schema(BaseSchema):
    """Schema for Scribe V1 Speech-to-Text (scribe_v1)"""

    model_id: str = Field(
        default="scribe_v1",
        description="Model ID: scribe_v1"
    )
    init_audio: Any = Field(
        ...,
        description="Audio file URL (supports MP3/WAV)"
    )


class ElevenMultilingualV2Schema(BaseSchema):
    """Schema for Eleven Multilingual V2 Text-to-Speech (eleven_multilingual_v2)"""

    model_id: str = Field(
        default="eleven_multilingual_v2",
        description="Model ID: eleven_multilingual_v2"
    )
    prompt: str = Field(
        ...,
        description="Text to be converted to speech"
    )
    voice_id: str = Field(
        ...,
        description="Selected voice identifier"
    )


class ElevenEnglishStsV2Schema(BaseSchema):
    """Schema for Eleven English STS V2 Voice Changer (eleven_english_sts_v2)"""

    model_id: str = Field(
        default="eleven_english_sts_v2",
        description="Model ID: eleven_english_sts_v2"
    )
    init_audio: Any = Field(
        ...,
        description="Audio file (MP3/WAV) or URL"
    )
    voice_id: str = Field(
        ...,
        description="Selected voice ID for transformation"
    )


class ElevenSoundEffectSchema(BaseSchema):
    """Schema for Eleven Sound Effect Generation (eleven_sound_effect)"""

    model_id: str = Field(
        default="eleven_sound_effect",
        description="Model ID: eleven_sound_effect"
    )
    prompt: str = Field(
        ...,
        description="Text description of desired sound effect"
    )
    time_in_seconds: Optional[int] = Field(
        None,
        alias="time in seconds",
        description="Duration in seconds (1-22)"
    )


class MusicV1Schema(BaseSchema):
    """Schema for Music V1 Generation (music_v1)"""

    model_id: str = Field(
        default="music_v1",
        description="Model ID: music_v1"
    )
    prompt: str = Field(
        ...,
        description="Text description for music generation"
    )
