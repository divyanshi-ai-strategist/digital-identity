import os
import httpx
from .exceptions import APIError

class LinkedinService:
    def __init__(self):
        self.token = os.getenv("LINKEDIN_ACCESS_TOKEN")
        self.base_url = os.getenv("LINKEDIN_URL")
        self.headers = {"Authorization":f"Bearer {self.token}"}
    
    async def get_my_profile(self):
        async with httpx.AsyncClient() as client:
            try:
                reponse= await client.get(
                f"{self.base_url}/v2/userinfo",
                headers=self.headers
                )
                reponse.raise_for_status()
                return reponse.json()
            except httpx.HTTPStatusError as e:
                raise APIError(str(e.response.text), e.response.status_code)