import os
import httpx
from .exceptions import APIError
class GitHubService:
    def __init__(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.base_url = os.getenv('GITHUB_URL')
        self.headers= {'Authorization': f"Bearer {self.token}"}
    
    async def get_my_repositories(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                f"{self.base_url}/user/repos?type=owner&sort=updated",
                headers=self.headers
                )
                response.raise_for_status()
                repos_data = response.json()
                return [
                    {
                    "name": r["name"],
                    "description": r["description"] or "No description provided.",
                    "stars": r["stargazers_count"],
                    "url": r["html_url"],
                    "tech": r["language"]
                    } for r in repos_data
                ]

            except httpx.HTTPStatusError as e:
                raise APIError(str(e.response.text), e.response.status_code)
