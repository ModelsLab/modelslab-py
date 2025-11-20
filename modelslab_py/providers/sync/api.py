from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.sync.schemas import Lipsync2Schema


class SyncProvider(BaseAPI):

    MODEL_LIPSYNC_2 = "lipsync-2"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "lipsync_2": SyncProvider.MODEL_LIPSYNC_2,
        }

    def lipsync_2(self, schema: Lipsync2Schema):
        endpoint = self.client.base_url + "v7/video-fusion/lip-sync"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
