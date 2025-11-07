from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.google.schemas import (
    Imagen4Schema,
    Imagen3Schema,
    Imagen40FastGenerateSchema,
    Imagen40UltraSchema,
    NanoBananaT2ISchema,
    NanoBananaSchema
)


class GoogleProvider(BaseAPI):

    MODEL_IMAGEN_4 = "imagen-4"
    MODEL_IMAGEN_3 = "imagen-3"
    MODEL_IMAGEN_40_FAST_GENERATE = "imagen-4.0-fast-generate"
    MODEL_IMAGEN_40_ULTRA = "imagen-4.0-ultra"
    MODEL_NANO_BANANA_T2I = "nano-banana-t2i"
    MODEL_NANO_BANANA = "nano-banana"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "imagen_4": GoogleProvider.MODEL_IMAGEN_4,
            "imagen_3": GoogleProvider.MODEL_IMAGEN_3,
            "imagen_40_fast_generate": GoogleProvider.MODEL_IMAGEN_40_FAST_GENERATE,
            "imagen_40_ultra": GoogleProvider.MODEL_IMAGEN_40_ULTRA,
            "nano_banana_t2i": GoogleProvider.MODEL_NANO_BANANA_T2I,
            "nano_banana": GoogleProvider.MODEL_NANO_BANANA,
        }

    def imagen_4(self, schema: Imagen4Schema):
        """Text-to-Image: Generate images with Imagen 4"""
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def imagen_3(self, schema: Imagen3Schema):
        """Text-to-Image: Generate images with Imagen 3"""
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def imagen_40_fast_generate(self, schema: Imagen40FastGenerateSchema):
        """Text-to-Image: Fast image generation with Imagen 4.0"""
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def imagen_40_ultra(self, schema: Imagen40UltraSchema):
        """Text-to-Image: High-quality image generation with Imagen 4.0 Ultra"""
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def nano_banana_t2i(self, schema: NanoBananaT2ISchema):
        """Text-to-Image: Generate images with Nano Banana"""
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def nano_banana(self, schema: NanoBananaSchema):
        """Image-to-Image: Blend or modify images with Nano Banana"""
        endpoint = self.client.base_url + "v7/images/image-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
