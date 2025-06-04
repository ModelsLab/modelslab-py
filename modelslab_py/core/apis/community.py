from modelslab_py.core.client import Client
import time
from modelslab_py.core.apis.base import BaseAPI 
from modelslab_py.schemas.community import *

class Community(BaseAPI):

    def __init__(self, client: Client = None, enterprise = False ,**kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        self.enterprise = enterprise
        if enterprise:
            self.base_url = self.client.base_url + "v1/enterprise/images/text2img/"
        else:
            self.base_url = self.client.base_url + "v6/images/text2img/"

        super().__init__()

    def text_to_image(self, schema: Text2Image):
        base_endpoint = self.base_url + "text2img"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def image_to_image(self, schema: Image2Image):
        base_endpoint = self.base_url + "img2img"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def inpainting(self, schema: Inpainting):
        base_endpoint = self.base_url + "inpaint"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def controlnet(self, schema: ControlNet):
        base_endpoint = self.base_url + "controlnet"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response