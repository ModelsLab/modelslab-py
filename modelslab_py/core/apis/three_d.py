from modelslab_py.schemas.threed import Text23D,Image23D
from modelslab_py.core.client import Client
import time
from modelslab_py.core.apis.base import BaseAPI

class Three_D(BaseAPI) :
    def __init__(self, client: Client = None, enterprise = False ,**kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        self.enterprise = enterprise
        if enterprise:
            self.base_url = self.client.base_url + "v1/enterprise/3d/"
        else:
            self.base_url = self.client.base_url + "v6/3d/"

        super().__init__()

    def text_to_3d(self,schema : Text23D):
        base_endpoint = self.base_url + "text_to_3d"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def image_to_3d(self,schema : Image23D):
        base_endpoint = self.base_url + "image_to_3d"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response