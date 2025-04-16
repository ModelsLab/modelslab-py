from modelslab.schemas.deepfake import (
    SingleVideoSwap,
    SpecificFaceSwap,
    MultipleFaceSwap,
    SpecificVideoSwap
)
from modelslab.core.client import Client
import time


class DeepFake:

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        self.base_url = self.client.base_url + "v6/deepfake/"

    def specific_face_swap(self, schema: SpecificFaceSwap):
        base_endpoint = self.base_url + "single_face_swap"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response

    def multiple_face_swap(self, schema: MultipleFaceSwap):
        base_endpoint = self.base_url + "multiple_face_swap"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def multiple_video_swap(self, schema: SpecificVideoSwap):
        base_endpoint = self.base_url + "specific_video_swap"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def single_video_swap(self, schema: SingleVideoSwap):
        base_endpoint = self.base_url + "single_video_swap"
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
    