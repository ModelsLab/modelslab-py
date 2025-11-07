from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.openai.schemas import Sora2Schema


class OpenAIProvider(BaseAPI):

    MODEL_SORA_2 = "sora-2"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "sora_2": OpenAIProvider.MODEL_SORA_2,
        }

    def sora_2(self, schema: Sora2Schema):
        """Text-to-Video: Generate videos from text with Sora 2"""
        endpoint = self.client.base_url + "v7/video-fusion/text-to-video"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
