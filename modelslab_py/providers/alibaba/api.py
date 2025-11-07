from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.alibaba.schemas import (
    Wan25I2VSchema,
    Wan25T2VSchema
)


class AlibabaProvider(BaseAPI):

    MODEL_WAN25_I2V = "wan2.5-i2v"
    MODEL_WAN25_T2V = "wan2.5-t2v"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "wan25_i2v": AlibabaProvider.MODEL_WAN25_I2V,
            "wan25_t2v": AlibabaProvider.MODEL_WAN25_T2V,
        }

    def wan25_i2v(self, schema: Wan25I2VSchema):
        """Image-to-Video: Convert image and audio to synchronized video"""
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def wan25_t2v(self, schema: Wan25T2VSchema):
        """Text-to-Video: Generate cinematic video from text and audio"""
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
