from typing import Optional, List, Dict, Any, Literal
from modelslab_py.schemas.base import BaseSchema
from pydantic import Field


class Text2Audio(BaseSchema):
    """
    Schema for text-to-audio conversion.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for audio generation."
    )
    init_audio: Optional[Any] = Field(
        None,
        description="Initial audio for the generation."
    )
    voice_id : Optional[str] = Field(
        None,
        description="Voice ID for the audio generation."
    )
    language: Optional[str] = Field(
        None,
        description="Language for the audio generation."
    )
    speed   : Optional[float] = Field(
        None,
        description="Speed of the audio generation."
    )
    temp   : Optional[float] = Field(
        None,
        description="Upload files in temp s3 directory for the audio generation."
    )
    base64  : Optional[str] = Field(
        None,
        description="Base64 encoded audio data."
    )

    stream: Optional[bool] = Field(
        None,
        description="Whether to stream the audio."
    )

class Text2Speech(BaseSchema):
    """
    Schema for text-to-speech conversion.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for speech generation."
    )
    
    voice_id : Optional[str] = Field(
        None,
        description="Voice ID for the speech generation."
    )

    language: Optional[str] = Field(
        None,
        description="Language for the speech generation."
    )

    speed   : Optional[float] = Field(
        None,
        description="Speed of the speech generation."
    )

    output_format: Optional[Literal["wav", "mp3"]] = Field(
        "wav",
        description="The format of the generated audio. Either 'wav' or 'mp3'. Defaults to 'wav'."
    )

    emotion: Optional[str] = Field(
        None,
        description="Emotion for the speech generation."
    )

    temp   : Optional[float] = Field(
        None,
        description="Upload files in temp s3 directory for the audio generation."
    )


class Voice2Voice(BaseSchema):
    """
    Schema for voice-to-voice conversion.
    """
    init_audio: Any = Field(
        ...,
        description="Initial audio for the voice conversion."
    )
    target_audio: Any = Field(
        ...,
        description="Target audio for the voice conversion."
    )
    
    base64:Optional[bool] = Field(
        None,
        description="Base64 encoded audio data."
    )
    temp   : Optional[float] = Field(
        None,
        description="Upload files in temp s3 directory for the audio generation."
    )
    stream: Optional[bool] = Field(
        None,
        description="Whether to stream the audio."
    )

class VoiceCover(BaseSchema):
    init_audio: Any = Field(
        ...,
        description="Initial audio for the voice cover."
    )
    model_id : Optional[str] = Field(
        None,
        description="Model ID for the voice cover."
    )

    pitch:Optional[str] = Field(
        None,
        description="Pitch for the voice cover."
    )

    algorithm: Optional[str] = Field(
        None,
        description="Algorithm for the voice cover."
    )

    rate : Optional[str] = Field(
        None,
        description="Rate for the voice cover."
    )

    seed : Optional[str] = Field(

        None,
        description="Seed for the voice cover."

    )

    emotion : Optional[str] = Field(
        "neutral",
        description="Emotion for the voice cover."
    )

    speed : Optional[float] = Field(
        None,
        description="Speed for the voice cover."
    )

    radius : Optional[float] = Field(
        None,
        description="Radius for the voice cover."
    )

    mix : Optional[float] = Field(
        None,
        description="Mix for the voice cover."
    )

    hop_length : Optional[int] = Field(
        None,
        description="Hop length for the voice cover."
    )

    originality : Optional[float] = Field(
        None,
        description="Originality for the voice cover."
    )

    lead_voice_volume_delta : Optional[int] = Field(
        None,
        description="Lead voice volume delta for the voice cover."
    )

    backup_voice_volume_delta : Optional[int] = Field(
        None,
        description="Backup voice volume delta for the voice cover."
    )

    instrument_volume_delta : Optional[int] = Field(
        None,
        description="Instrument volume delta for the voice cover."
    )

    reverb_size : Optional[float] = Field(
        None,
        description="Reverb size for the voice cover."
    )

    wetness : Optional[float] = Field(
        None,
        description="Wetness for the voice cover."
    )

    dryness : Optional[float] = Field(
        None,
        description="Dryness for the voice cover."
    )

    damping : Optional[float] = Field(
        None,
        description="Damping for the voice cover."
    )

    base64: Optional[bool] = Field(
        None,
        description="Base64 encoded audio data."
    )

    temp   : Optional[float] = Field(
        None,
        description="Upload files in temp s3 directory for the audio generation."
    )

class MusicGenSchema(BaseSchema):
    """
    Schema for music generation.
    """
    prompt: str = Field(
        ...,
        description="Text prompt for music generation."
    )
    init_audio: Optional[Any] = Field(
        None,
        description="Initial audio for the music generation."
    )
    
    output_format: Optional[Literal["wav", "mp3", "flac"]] = Field(
        "wav",
        description="The format of the generated audio. Either 'wav', 'mp3', or 'flac'. Defaults to 'wav'."
    )

    bitrate: Optional[Literal["128k", "192k", "320k"]] = Field(
        "320k",
        description="Bitrate of the generated audio. Options: '128k', '192k', '320k' Defaults to `320k`."
    )
    
    base64: Optional[str] = Field(
        None,
        description="Base64 encoded audio data."
    )
    
    temp   : Optional[float] = Field(
        None,
        description="Upload files in temp s3 directory for the audio generation."
    )
    max_new_token : Optional[int] = Field(
        None,
        description="Maximum number of new tokens for the music generation."
    )

    sampling_rate : Optional[int] = Field(
        None,
        description="Sampling rate for the music generation."
    )


class LyricsGenerator(BaseSchema):
    prompt: str = Field(\
        ...,
        description="Text prompt for lyrics generation."
    )


class SongGenerator(BaseSchema):
    lyrics_generation:Optional[bool] = Field(
        None,
        description="Whether to generate lyrics."
    )
    init_audio: Optional[Any] = Field(
        None,
        description="Initial audio for the song generation."
    )
    prompt: str = Field(
        ...,
        description="Text prompt for song generation."
    )
    lyrics : Optional[str] = Field(
        None,
        description="Lyrics for the song generation."
    )

class Speech2Text(BaseSchema):
    """
    Schema for speech-to-text conversion.
    """
    audio_url : str = Field(
        ...,
        description="Audio URL for speech-to-text conversion."
    )

    input_language : Optional[str] = Field(
        None,
        description="Input language for speech-to-text conversion."
    )

    timestamp_level : Optional[Literal["word", "sentence"]] = Field(
        None,
        description="Timestamp level for speech-to-text conversion."
    )

class SFX(BaseSchema):
    prompt: str = Field(
        ...,
        description="Text prompt for sound effect generation."
    )

    duration : Optional[int] = Field(
        None,
        description="Duration for the sound effect generation."
    )

    output_format: Optional[Literal["wav", "mp3", "flac"]] = Field(
        "wav",
        description="The format of the generated audio. Either 'wav', 'mp3', or 'flac'. Defaults to 'wav'."
    )

    bitrate: Optional[Literal["128k", "192k", "320k"]] = Field(
        "320k",
        description="Bitrate of the generated audio. Options: '128k', '192k', '320k' Defaults to `320k`."
    )

    temp : Optional[bool]  = Field(
        None,
        description="Upload files in temp s3 directory for the sound effect generation."
    )