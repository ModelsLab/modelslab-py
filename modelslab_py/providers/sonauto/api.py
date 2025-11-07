from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.sonauto.schemas import (
    SonautoSongSchema,
    SongExtenderSchema,
    SongInpaintSchema
)


class SonautoProvider(BaseAPI):

    MODEL_SONAUTO_SONG = "sonauto_song"
    MODEL_SONG_EXTENDER = "song-extender"
    MODEL_SONG_INPAINT = "song-inpaint"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "sonauto_song": SonautoProvider.MODEL_SONAUTO_SONG,
            "song_extender": SonautoProvider.MODEL_SONG_EXTENDER,
            "song_inpaint": SonautoProvider.MODEL_SONG_INPAINT,
        }

    def sonauto_song(self, schema: SonautoSongSchema):
        """Music Generation: Generate songs from text descriptions"""
        endpoint = self.client.base_url + "v7/voice/music-gen"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def song_extender(self, schema: SongExtenderSchema):
        """Song Extension: Extend existing songs with AI"""
        endpoint = self.client.base_url + "v7/voice/song-extender"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def song_inpaint(self, schema: SongInpaintSchema):
        """Song Inpainting: Apply voice cloning to specific song sections"""
        endpoint = self.client.base_url + "v7/voice/song-inpaint"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
