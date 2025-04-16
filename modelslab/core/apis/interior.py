from modelslab.schemas.interior import (
    ExteriorSchema,
    ScenarioSchema,
    FloorSchema,
    RoomDecoratorSchema,
    InteriorSchema

)
from modelslab.core.client import Client
import time

class Interior :

    def __init__(self,client : Client =None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        self.base_url = self.client.base_url + "v6/interior/"
        
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
    
    def fetch(self, id : str):
        base_endpoint = self.base_url + "fetch" + "/" + id
        response = None
        for i in range(self.client.fetch_retry):
            response = self.client.post(base_endpoint, data={
                "key" : self.client.api_key
            })

            if response["status"] == "success":
                break
            else:
                time.sleep(self.client.fetch_timeout)
        
        return response