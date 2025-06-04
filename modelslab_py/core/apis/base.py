import time
from modelslab_py.core.client import Client
from modelslab_py.schemas.base import BaseSchema
from typing import Any, Dict, Optional
from pydantic import Field


class BaseAPI:
    """
    Base class for all APIs in the ModelsLab framework.
    This class provides a common interface and shared functionality for all API classes.
    """
    client : Client = None
    enterprise : bool = False
    base_url : str = None
    kwargs : Dict[str, Any] = None
    
    def __init__(self):
        """
        Initialize the BaseAPI instance.
        """
        pass

    def fetch(self, id: str):
        base_endpoint = self.base_url + "fetch" + "/" + id
        response = None
        for i in range(self.client.fetch_retry):
            response = self.client.post(base_endpoint, data={
                "key": self.client.api_key
            })

            if response["status"] == "success":
                break
            else:
                time.sleep(self.client.fetch_timeout)

        return response
    
    def system_details(self):
        if  not self.enterprise:
            raise ValueError("System details are only available for enterprise users.")
        
        base_endpoint = self.base_url + "system_details"
        response = self.client.post(base_endpoint, data={
            "key": self.client.api_key
        })

        return response
    
    def restart(self):
        if  not self.enterprise:
            raise ValueError("System details are only available for enterprise users.")
        
        base_endpoint = self.base_url + "restart_server"
        response = self.client.post(base_endpoint, data={
            "key": self.client.api_key
        })

        return response
    
    def update(self):
        if  not self.enterprise:
            raise ValueError("System details are only available for enterprise users.")
        
        base_endpoint = self.base_url + "update"
        response = self.client.post(base_endpoint, data={
            "key": self.client.api_key
        })

        return response
    
    def clear_cache(self):
        if  not self.enterprise:
            raise ValueError("System details are only available for enterprise users.")
        
        base_endpoint = self.base_url + "clear_cache"
        response = self.client.post(base_endpoint, data={
            "key": self.client.api_key
        })

        return response
    
    def clear_queue(self):
        if  not self.enterprise:
            raise ValueError("System details are only available for enterprise users.")
        
        base_endpoint = self.base_url + "clear_queue"
        response = self.client.post(base_endpoint, data={
            "key": self.client.api_key
        })

        return response

    