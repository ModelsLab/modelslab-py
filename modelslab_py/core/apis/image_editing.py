from modelslab_py.core.client import Client
import time
from modelslab_py.core.apis.base import BaseAPI 
from modelslab_py.schemas.image_editing import *

class Image_editing(BaseAPI):

    def __init__(self, client: Client = None, enterprise = False ,**kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        self.enterprise = enterprise
        if enterprise:
            self.base_url = self.client.base_url + "v1/enterprise/image_editing/"
        else:
            self.base_url = self.client.base_url + "v6/image_editing/"

        super().__init__()

    def outpainting(self, schema: OutpaintingSchema):
        base_endpoint = self.base_url + "outpaint"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def background_remover(self, schema: BackgroundRemoverSchema):
        base_endpoint = self.base_url + "removebg_mask"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def super_resolution(self, schema: SuperResolutionSchema):
        base_endpoint = self.base_url + "super_resolution"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def fashion(self, schema: FashionSchema):
        base_endpoint = self.base_url + "fashion"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def object_remover(self, schema: ObjectRemovalSchema):
        base_endpoint = self.base_url + "object_removal"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def facegen(self, schema: FacegenSchema):
        base_endpoint = self.base_url + "face_gen"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def inpainting(self, schema: InpaintingSchema):
        base_endpoint = self.base_url + "inpaint"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def headshot(self, schema: HeadshotSchema):
        base_endpoint = self.base_url + "head_shot"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def flux_headshot(self, schema: FluxHeadshotSchema):
        base_endpoint = self.base_url + "flux_headshot"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response