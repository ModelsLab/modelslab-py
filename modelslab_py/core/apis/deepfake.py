from modelslab_py.schemas.deepfake import (
    SingleVideoSwap,
    SpecificFaceSwap,
    MultipleFaceSwap,
    SpecificVideoSwap
)
from modelslab_py.core.client import Client
import time
from modelslab_py.core.apis.base import BaseAPI 

class DeepFake(BaseAPI):

    def __init__(self, client: Client = None, enterprise = False ,**kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        self.enterprise = enterprise
        if enterprise:
            self.base_url = self.client.base_url + "v1/enterprise/deepfake/"
        else:
            self.base_url = self.client.base_url + "v6/deepfake/"

        super().__init__()

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