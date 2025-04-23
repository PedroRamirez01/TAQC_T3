import httpx
import os

BASE_URL = "https://automation-portal-bootcamp.vercel.app/"
TOKEN = os.getenv("TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

async def get_user_by_email(email):
    if not email:
        return None
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}api/user?email={email}", headers=HEADERS)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

async def delete_user_by_id(email):
    user = await get_user_by_email(email)
    if user is None:
        return None
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(f"{BASE_URL}api/user/{user['id']}", headers=HEADERS)
            return response.status_code
        except httpx.RequestError:
            return None