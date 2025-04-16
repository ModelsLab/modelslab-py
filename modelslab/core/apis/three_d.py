from modelslab.schemas.threed import Text23D,Image23D
from modelslab.core.client import Client
import time

class Three_D :
    def __init__(self,client : Client =None, **kwargs):
        self.client = client
        self.kwargs = kwargs
        self.base_url = self.client.base_url + "v6/3d/"

    def text_to_3d(self,schema : Text23D):
        base_endpoint = self.base_url + "text_to_3d"
        data = schema.dict()
        response = self.client.post(base_endpoint, data=data)
        return response
    
    def image_to_3d(self,schema : Image23D):
        base_endpoint = self.base_url + "image_to_3d"
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