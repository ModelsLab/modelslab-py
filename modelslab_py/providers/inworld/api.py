from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.inworld.schemas import InworldTts1Schema


class InworldProvider(BaseAPI):

    MODEL_INWORLD_TTS_1 = "inworld-tts-1"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "inworld_tts_1": InworldProvider.MODEL_INWORLD_TTS_1,
        }

    def inworld_tts_1(self, schema: InworldTts1Schema):
        """Text-to-Speech: Convert text to speech with voice cloning across 11 languages"""
        endpoint = self.client.base_url + "v7/voice/text-to-speech"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
