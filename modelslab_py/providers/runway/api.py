from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.runway.schemas import (
    Gen4ImageSchema,
    Gen4ImageTurboSchema,
    Gen4AlephSchema
)


class RunwayProvider(BaseAPI):

    MODEL_GEN4_IMAGE = "gen4_image"
    MODEL_GEN4_IMAGE_TURBO = "gen4_image_turbo"
    MODEL_GEN4_ALEPH = "gen4_aleph"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "gen4_image": RunwayProvider.MODEL_GEN4_IMAGE,
            "gen4_image_turbo": RunwayProvider.MODEL_GEN4_IMAGE_TURBO,
            "gen4_aleph": RunwayProvider.MODEL_GEN4_ALEPH,
        }

    def gen4_image(self, schema: Gen4ImageSchema):
        """Text-to-Image: Generate images from text with specified aspect ratio"""
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def gen4_image_turbo(self, schema: Gen4ImageTurboSchema):
        """Image-to-Image: Transform images with reference-based consistency"""
        endpoint = self.client.base_url + "v7/images/image-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def gen4_aleph(self, schema: Gen4AlephSchema):
        """Video-to-Video: Transform videos with AI"""
        endpoint = self.client.base_url + "v7/video-fusion/video-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
