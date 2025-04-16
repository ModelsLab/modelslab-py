import os

class Client:
    def __init__(self,api_key:str,fetch_retry:int=10,fetch_timeout:int=2):
        self.api_key = self._load_api_key(api_key)
        self.base_url = "https://modelslab.com/api/"
        self.fetch_retry = fetch_retry
        self.fetch_timeout = fetch_timeout

    def _load_api_key(self, api_key: str) -> str:

        if not api_key:
            api_key = os.getenv("API_KEY")
            if not api_key:
                raise ValueError("API key is required.")
        return api_key
    
    def post(self, endpoint: str, data: dict):
        # Placeholder for the actual POST request implementation
        pass

    def get(self, endpoint: str):   
        # Placeholder for the actual GET request implementation
        pass