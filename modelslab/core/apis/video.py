

from modelslab.core.client import Client
import time
from modelslab.schemas.video import Text2Video, Image2Video


class Video:
    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        self.base_url = self.client.base_url + "v6/video/"

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
    
    def fetch(self, id: str):
        base_endpoint = self.base_url + "fetch" + "/" + id
        response = None
        for i in range(self.client.fetch_retry):
            response = self.client.post(base_endpoint, data={
                "key": self.client.api_key
            })

            if response["status"] == "success":
                break
            else:
                time.sleep(self.client.fetch_timeout)

        return response