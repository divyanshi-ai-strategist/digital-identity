from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from services.github_service import GitHubService
from services.linkedin_service import LinkedinService
from services.exceptions import APIError

load_dotenv()
app = FastAPI()
github_svc = GitHubService()
linkedin_svc = LinkedinService()

@app.get("/")
async def root():
    return {"message":"Welcome to digital Identity"}

@app.get("/profile")
async def linkedin_profile():
    try:
        return await linkedin_svc.get_my_profile()
    except APIError as e:
        raise HTTPException (status_code=e.status_code, detail=str(e.message))
@app.get("/projects")
async def github_projects():
    try:
        return await github_svc.get_my_repositories()
    except APIError as e:
        raise HTTPException (status_code=e.status_code, detail=str(e.message))
