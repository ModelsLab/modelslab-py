import os
import requests
try:
    import aiohttp
    import asyncio
except ImportError:
    aiohttp = None
    asyncio = None

class Client:
    def __init__(self,api_key:str,fetch_retry:int=10,fetch_timeout:int=60):
        self.api_key = self._load_api_key(api_key)
        self.base_url = "https://modelslab.com/api/"
        self.fetch_retry = fetch_retry
        self.fetch_timeout = fetch_timeout
        self._session = None
        self._timeout = None

    def _load_api_key(self, api_key: str) -> str:

        if not api_key:
            api_key = os.getenv("API_KEY")
            if not api_key:
                raise ValueError("API key is required.")
        return api_key

    def post(self, endpoint: str, data: dict = None):
        ## just do post request with data to endpoint
        data = {"key": self.api_key, **(data or {})}
        response = requests.post(
            endpoint,
            json=data,
        )
        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
        return response.json()

    async def async_post(self, endpoint: str, data: dict = None):
        if aiohttp is None:
            raise ImportError("aiohttp is required for async support. Install with: pip install 'modelslab-py[async]'")

        data = {"key": self.api_key, **(data or {})}

        # Create session if it doesn't exist
        if self._session is None:
            timeout = aiohttp.ClientTimeout(total=self.fetch_timeout)
            self._session = aiohttp.ClientSession(timeout=timeout)

        try:
            async with self._session.post(endpoint, json=data) as response:
                if response.status != 200:
                    text = await response.text()
                    raise Exception(f"Request failed with status code {response.status}: {text}")
                return await response.json()
        except aiohttp.ClientError as e:
            raise Exception(f"Network error occurred: {str(e)}") from e
        except asyncio.TimeoutError as e:
            raise Exception(f"Request timed out after {self.fetch_timeout} seconds") from e

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        return False  # Don't suppress exceptions
