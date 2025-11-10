from modelslab_py.schemas.interior import (
    ExteriorSchema,
    ScenarioSchema,
    FloorSchema,
    RoomDecoratorSchema,
    InteriorSchema,
    ObjectRemovalSchema,
    InteriorMixerSchema

)
from modelslab_py.core.client import Client
import time
from modelslab_py.core.apis.base import BaseAPI

class Interior(BaseAPI) :

    def __init__(self, client: Client = None, enterprise = False ,**kwargs):
        self.client = client
        self.kwargs = kwargs
        if not self.client:
            raise ValueError("Client is required.")
        self.enterprise = enterprise
        if enterprise:
            self.base_url = self.client.base_url + "v1/enterprise/interior/"
        else:
            self.base_url = self.client.base_url + "v6/interior/"

        super().__init__()
        
    def interior(self,schema : InteriorSchema):
        base_endpoint = self.base_url + "make"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_interior(self,schema : InteriorSchema):
        base_endpoint = self.base_url + "make"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def room_decorator(self,schema : RoomDecoratorSchema):
        base_endpoint = self.base_url + "room_decorator"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_room_decorator(self,schema : RoomDecoratorSchema):
        base_endpoint = self.base_url + "room_decorator"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def floor(self,schema : FloorSchema):
        base_endpoint = self.base_url + "floor_planning"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_floor(self,schema : FloorSchema):
        base_endpoint = self.base_url + "floor_planning"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def scenario(self,schema : ScenarioSchema):
        base_endpoint = self.base_url + "scenario"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_scenario(self,schema : ScenarioSchema):
        base_endpoint = self.base_url + "scenario"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def exterior_restorer(self,schema : ExteriorSchema):
        base_endpoint = self.base_url + "exterior_restorer"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_exterior_restorer(self,schema : ExteriorSchema):
        base_endpoint = self.base_url + "exterior_restorer"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def object_removal(self, schema: ObjectRemovalSchema):
        base_endpoint = self.base_url + "object_removal"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_object_removal(self, schema: ObjectRemovalSchema):
        base_endpoint = self.base_url + "object_removal"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response

    def interior_mixer(self, schema: InteriorMixerSchema):
        base_endpoint = self.base_url + "interior_mixer"
        data = schema.dict(exclude_none=True)
        response = self.client.post(base_endpoint, data=data)
        return response

    async def async_interior_mixer(self, schema: InteriorMixerSchema):
        base_endpoint = self.base_url + "interior_mixer"
        data = schema.dict(exclude_none=True)
        response = await self.client.async_post(base_endpoint, data=data)
        return response
