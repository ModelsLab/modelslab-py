from modelslab_py.core.client import Client
from modelslab_py.core.apis.base import BaseAPI
from modelslab_py.providers.bfl.schemas import (
    FluxPro1752000026Schema,
    FluxPro11Schema,
    FluxPro11UltraSchema,
    FluxKontextProSchema,
    Flux2ProSchema,
    Flux2ProImageEditingSchema
)


class BFLProvider(BaseAPI):

    MODEL_FLUX_PRO_1752000026 = "flux-pro-1752000026"
    MODEL_FLUX_PRO_11 = "flux-pro-1.1"
    MODEL_FLUX_PRO_11_ULTRA = "flux-pro-1.1-ultra"
    MODEL_FLUX_KONTEXT_PRO = "flux-kontext-pro"
    MODEL_FLUX_2_PRO = "flux-2-pro"

    def __init__(self, client: Client = None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        super().__init__()

    @staticmethod
    def get_model_ids():
        return {
            "flux_pro_1752000026": BFLProvider.MODEL_FLUX_PRO_1752000026,
            "flux_pro_11": BFLProvider.MODEL_FLUX_PRO_11,
            "flux_pro_11_ultra": BFLProvider.MODEL_FLUX_PRO_11_ULTRA,
            "flux_kontext_pro": BFLProvider.MODEL_FLUX_KONTEXT_PRO,
            "flux_2_pro": BFLProvider.MODEL_FLUX_2_PRO,
        }

    def flux_pro_1752000026(self, schema: FluxPro1752000026Schema):
        endpoint = self.client.base_url + "v6/images/text2img"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def flux_pro_11(self, schema: FluxPro11Schema):
        endpoint = self.client.base_url + "v6/images/text2img"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def flux_pro_11_ultra(self, schema: FluxPro11UltraSchema):
        endpoint = self.client.base_url + "v6/images/text2img"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def flux_kontext_pro(self, schema: FluxKontextProSchema):
        endpoint = self.client.base_url + "v7/images/image-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def flux_2_pro(self, schema: Flux2ProSchema):
        endpoint = self.client.base_url + "v7/images/text-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response

    def flux_2_pro_image_editing(self, schema: Flux2ProImageEditingSchema):
        endpoint = self.client.base_url + "v7/images/image-to-image"
        data = schema.dict(exclude_none=True)
        response = self.client.post(endpoint, data=data)
        return response
