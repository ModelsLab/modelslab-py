from modelslab_py.core.client import Client
import time
from modelslab_py.core.apis.base import BaseAPI 
from modelslab_py.schemas.audio import *

class Audio(BaseAPI):

    def __init__(self, client: Client = None, enterprise = False ,**kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        self.enterprise = enterprise
        if enterprise:
            self.base_url = self.client.base_url + "v1/enterprise/voice/"
        else:
            self.base_url = self.client.base_url + "v6/voice/"

        super().__init__()
    
    def text_to_audio(self, schema: Text2Audio):
        base_endpoint = self.base_url + "text_to_audio"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def text_to_speech(self, schema: Text2Speech):
        base_endpoint = self.base_url + "text_to_speech"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def voice2voice(self, schema: Voice2Voice):
        base_endpoint = self.base_url + "voice_to_voice"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def voice_cover(self, schema: VoiceCover):
        base_endpoint = self.base_url + "voice_cover"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def music_gen(self, schema: MusicGenSchema):
        base_endpoint = self.base_url + "music_gen"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def lyrics_gen(self, schema: LyricsGenerator):
        base_endpoint = self.base_url + "lyrics_generator"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response

    def song_generator(self, schema: SongGenerator):
        base_endpoint = self.base_url + "song_generator"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def speech_to_text(self, schema: Speech2Text):
        base_endpoint = self.base_url + "speech_to_text"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def sfx_gen(self, schema: SFX):
        base_endpoint = self.base_url + "sfx"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response