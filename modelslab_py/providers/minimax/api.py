from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.minimax.schemas import (
    Hailuo23T2VSchema,
    Hailuo02T2VSchema,
    Hailuo23I2VSchema,
    Hailuo23FastI2VSchema,
    Hailuo02I2VSchema,
    Hailuo02StartEndFrameSchema
)


class MinimaxProvider(BaseAPI):

    MODEL_HAILUO_23_T2V = "Hailuo-2.3-t2v"
    MODEL_HAILUO_02_T2V = "Hailuo-02-t2v"
    MODEL_HAILUO_23_I2V = "Hailuo-2.3-i2v"
    MODEL_HAILUO_23_FAST_I2V = "Hailuo-2.3-Fast-i2v"
    MODEL_HAILUO_02_I2V = "Hailuo-02-i2v"
    MODEL_HAILUO_02_START_END_FRAME = "Hailuo-02-start-end-frame"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "hailuo_23_t2v": MinimaxProvider.MODEL_HAILUO_23_T2V,
            "hailuo_02_t2v": MinimaxProvider.MODEL_HAILUO_02_T2V,
            "hailuo_23_i2v": MinimaxProvider.MODEL_HAILUO_23_I2V,
            "hailuo_23_fast_i2v": MinimaxProvider.MODEL_HAILUO_23_FAST_I2V,
            "hailuo_02_i2v": MinimaxProvider.MODEL_HAILUO_02_I2V,
            "hailuo_02_start_end_frame": MinimaxProvider.MODEL_HAILUO_02_START_END_FRAME,
        }

    def hailuo_23_t2v(self, schema: Hailuo23T2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def hailuo_02_t2v(self, schema: Hailuo02T2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def hailuo_23_i2v(self, schema: Hailuo23I2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def hailuo_23_fast_i2v(self, schema: Hailuo23FastI2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def hailuo_02_i2v(self, schema: Hailuo02I2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def hailuo_02_start_end_frame(self, schema: Hailuo02StartEndFrameSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
