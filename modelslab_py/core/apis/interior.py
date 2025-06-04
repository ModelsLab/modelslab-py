from modelslab_py.schemas.interior import (
    ExteriorSchema,
    ScenarioSchema,
    FloorSchema,
    RoomDecoratorSchema,
    InteriorSchema

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
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def room_decorator(self,schema : RoomDecoratorSchema):
        base_endpoint = self.base_url + "room_decorator"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response

    def floor(self,schema : FloorSchema):
        base_endpoint = self.base_url + "floor_planning"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def scenario(self,schema : ScenarioSchema):
        base_endpoint = self.base_url + "scenario"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def exterior_restorer(self,schema : ExteriorSchema):
        base_endpoint = self.base_url + "exterior_restorer"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def room_decorator(self,schema : RoomDecoratorSchema):
        base_endpoint = self.base_url + "room_decorator"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    