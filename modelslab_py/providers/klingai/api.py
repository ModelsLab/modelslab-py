from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.klingai.schemas import (
    KlingV21I2VSchema,
    KlingV25TurboI2VSchema,
    KlingV25TurboT2VSchema,
    KlingV2MasterT2VSchema,
    KlingV2MasterI2VSchema,
    KlingV21MasterT2VSchema,
    KlingV21MasterI2VSchema
)


class KlingAIProvider(BaseAPI):

    MODEL_KLING_V21_I2V = "kling-v2-1-i2v"
    MODEL_KLING_V25_TURBO_I2V = "Kling-V2-5-Turbo-i2v"
    MODEL_KLING_V25_TURBO_T2V = "kling-v2-5-turbo-t2v"
    MODEL_KLING_V2_MASTER_T2V = "kling-v2-master-t2v"
    MODEL_KLING_V2_MASTER_I2V = "kling-v2-master-i2v"
    MODEL_KLING_V21_MASTER_T2V = "kling-v2-1-master-t2v"
    MODEL_KLING_V21_MASTER_I2V = "kling-v2-1-master-i2v"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "kling_v21_i2v": KlingAIProvider.MODEL_KLING_V21_I2V,
            "kling_v25_turbo_i2v": KlingAIProvider.MODEL_KLING_V25_TURBO_I2V,
            "kling_v25_turbo_t2v": KlingAIProvider.MODEL_KLING_V25_TURBO_T2V,
            "kling_v2_master_t2v": KlingAIProvider.MODEL_KLING_V2_MASTER_T2V,
            "kling_v2_master_i2v": KlingAIProvider.MODEL_KLING_V2_MASTER_I2V,
            "kling_v21_master_t2v": KlingAIProvider.MODEL_KLING_V21_MASTER_T2V,
            "kling_v21_master_i2v": KlingAIProvider.MODEL_KLING_V21_MASTER_I2V,
        }

    def kling_v21_i2v(self, schema: KlingV21I2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def kling_v25_turbo_i2v(self, schema: KlingV25TurboI2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def kling_v25_turbo_t2v(self, schema: KlingV25TurboT2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def kling_v2_master_t2v(self, schema: KlingV2MasterT2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def kling_v2_master_i2v(self, schema: KlingV2MasterI2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def kling_v21_master_t2v(self, schema: KlingV21MasterT2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def kling_v21_master_i2v(self, schema: KlingV21MasterI2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
