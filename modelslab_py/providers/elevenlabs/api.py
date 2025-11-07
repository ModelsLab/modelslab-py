from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.elevenlabs.schemas import (
    ScribeV1Schema,
    ElevenMultilingualV2Schema,
    ElevenEnglishStsV2Schema,
    ElevenSoundEffectSchema,
    MusicV1Schema
)


class ElevenLabsProvider(BaseAPI):

    MODEL_SCRIBE_V1 = "scribe_v1"
    MODEL_ELEVEN_MULTILINGUAL_V2 = "eleven_multilingual_v2"
    MODEL_ELEVEN_ENGLISH_STS_V2 = "eleven_english_sts_v2"
    MODEL_ELEVEN_SOUND_EFFECT = "eleven_sound_effect"
    MODEL_MUSIC_V1 = "music_v1"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "scribe_v1": ElevenLabsProvider.MODEL_SCRIBE_V1,
            "eleven_multilingual_v2": ElevenLabsProvider.MODEL_ELEVEN_MULTILINGUAL_V2,
            "eleven_english_sts_v2": ElevenLabsProvider.MODEL_ELEVEN_ENGLISH_STS_V2,
            "eleven_sound_effect": ElevenLabsProvider.MODEL_ELEVEN_SOUND_EFFECT,
            "music_v1": ElevenLabsProvider.MODEL_MUSIC_V1,
        }

    def scribe_v1(self, schema: ScribeV1Schema):
        """Speech-to-Text: Convert audio to text with speaker diarization"""
        endpoint = self.client.base_url + "v7/voice/speech-to-text"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def eleven_multilingual_v2(self, schema: ElevenMultilingualV2Schema):
        """Text-to-Speech: Convert text to speech in 29 languages"""
        endpoint = self.client.base_url + "v7/voice/text-to-speech"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def eleven_english_sts_v2(self, schema: ElevenEnglishStsV2Schema):
        """Speech-to-Speech: Transform voices with voice changer"""
        endpoint = self.client.base_url + "v7/voice/speech-to-speech"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def eleven_sound_effect(self, schema: ElevenSoundEffectSchema):
        """Sound Generation: Create sound effects from text descriptions"""
        endpoint = self.client.base_url + "v7/voice/sound-generation"
        data = schema.dict(exclude_none=True, by_alias=True)
        response = self.client.post(endpoint, data=data)
        return response

    def music_v1(self, schema: MusicV1Schema):
        """Music Generation: Generate music from text descriptions"""
        endpoint = self.client.base_url + "v7/voice/music-gen"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
