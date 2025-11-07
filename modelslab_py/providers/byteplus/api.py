from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.byteplus.schemas import (
    SeeDreamT2ISchema,
    SeeDanceT2VSchema,
    SeeDanceI2VSchema,
    SeeEditI2ISchema,
    SeeDream4Schema,
    SeeDream4I2ISchema,
    SeeDance10ProI2VSchema,
    OmniHumanSchema,
    OmniHuman15Schema,
    SeeDance10ProFastI2VSchema,
    SeeDance10ProFastT2VSchema
)


class BytePlusProvider(BaseAPI):

    MODEL_SEEDREAM_T2I = "seedream-t2i"
    MODEL_SEEDANCE_T2V = "seedance-t2v"
    MODEL_SEEDANCE_I2V = "seedance-i2v"
    MODEL_SEEDEDIT_I2I = "seededit-i2i"
    MODEL_SEEDREAM_4 = "seedream-4"
    MODEL_SEEDREAM_4_I2I = "seedream-4.0-i2i"
    MODEL_SEEDANCE_10_PRO_I2V = "seedance-1.0-pro-i2v"
    MODEL_OMNI_HUMAN = "omni-human"
    MODEL_OMNI_HUMAN_15 = "omni-human-1.5"
    MODEL_SEEDANCE_10_PRO_FAST_I2V = "seedance-1.0-pro-fast-i2v"
    MODEL_SEEDANCE_10_PRO_FAST_T2V = "seedance-1.0-pro-fast-t2v"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "seedream_t2i": BytePlusProvider.MODEL_SEEDREAM_T2I,
            "seedance_t2v": BytePlusProvider.MODEL_SEEDANCE_T2V,
            "seedance_i2v": BytePlusProvider.MODEL_SEEDANCE_I2V,
            "seededit_i2i": BytePlusProvider.MODEL_SEEDEDIT_I2I,
            "seedream_4": BytePlusProvider.MODEL_SEEDREAM_4,
            "seedream_4_i2i": BytePlusProvider.MODEL_SEEDREAM_4_I2I,
            "seedance_10_pro_i2v": BytePlusProvider.MODEL_SEEDANCE_10_PRO_I2V,
            "omni_human": BytePlusProvider.MODEL_OMNI_HUMAN,
            "omni_human_15": BytePlusProvider.MODEL_OMNI_HUMAN_15,
            "seedance_10_pro_fast_i2v": BytePlusProvider.MODEL_SEEDANCE_10_PRO_FAST_I2V,
            "seedance_10_pro_fast_t2v": BytePlusProvider.MODEL_SEEDANCE_10_PRO_FAST_T2V,
        }

    def seedream_t2i(self, schema: SeeDreamT2ISchema):
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seedance_t2v(self, schema: SeeDanceT2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seedance_i2v(self, schema: SeeDanceI2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seededit_i2i(self, schema: SeeEditI2ISchema):
        endpoint = self.client.base_url + "v7/images/image-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seedream_4(self, schema: SeeDream4Schema):
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seedream_4_i2i(self, schema: SeeDream4I2ISchema):
        endpoint = self.client.base_url + "v7/images/image-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seedance_10_pro_i2v(self, schema: SeeDance10ProI2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def omni_human(self, schema: OmniHumanSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def omni_human_15(self, schema: OmniHuman15Schema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seedance_10_pro_fast_i2v(self, schema: SeeDance10ProFastI2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/image-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def seedance_10_pro_fast_t2v(self, schema: SeeDance10ProFastT2VSchema):
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
