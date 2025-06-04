

from modelslab_py.core.client import Client
import time
from modelslab_py.schemas.video import Text2Video, Image2Video
from modelslab_py.core.apis.base import BaseAPI


class Video(BaseAPI):
    def __init__(self, client: Client = None, enterprise = False ,**kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        self.enterprise = enterprise
        if enterprise:
            self.base_url = self.client.base_url + "v1/enterprise/video/"
        else:
            self.base_url = self.client.base_url + "v6/video/"

        super().__init__()

    def text_to_video(self, schema: Text2Video):
        base_endpoint = self.base_url + "text2video"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response

    def image_to_video(self, schema: Image2Video):
        base_endpoint = self.base_url + "img2video"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response