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
            self.base_url = self.client.base_url + "v1/enterprise/images/"
        else:
            self.base_url = self.client.base_url + "v6/images/"

        super().__init__()

    def text_to_image(self, schema: Text2Image):
        base_endpoint = self.base_url + "text2img"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_text_to_image(self, schema: Text2Image):
        base_endpoint = self.base_url + "text2img"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def image_to_image(self, schema: Image2Image):
        base_endpoint = self.base_url + "img2img"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_image_to_image(self, schema: Image2Image):
        base_endpoint = self.base_url + "img2img"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def inpainting(self, schema: Inpainting):
        base_endpoint = self.base_url + "inpaint"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_inpainting(self, schema: Inpainting):
        base_endpoint = self.base_url + "inpaint"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def controlnet(self, schema: ControlNet):
        base_endpoint = self.base_url + "controlnet"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_controlnet(self, schema: ControlNet):
        base_endpoint = self.base_url + "controlnet"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def qwen_text_to_image(self, schema: QwenText2Image):
        if not self.enterprise:
            raise ValueError("Qwen API is only available for enterprise users.")
        base_endpoint = self.client.base_url + "v1/enterprise/qwen/text2img"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_qwen_text_to_image(self, schema: QwenText2Image):
        if not self.enterprise:
            raise ValueError("Qwen API is only available for enterprise users.")
        base_endpoint = self.client.base_url + "v1/enterprise/qwen/text2img"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response