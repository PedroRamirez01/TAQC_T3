import httpx
import os
from config.config import Config

URL_BASE = Config().URL_BASE
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
            response = await client.get(f"{URL_BASE}api/user?email={email}", headers=HEADERS)
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
            response = await client.delete(f"{URL_BASE}api/user/{user['id']}", headers=HEADERS)
            return response.status_code
        except httpx.RequestError:
            return None
        
async def verify_order_exists(order_id: str):
    if not order_id:
        return False
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE}api/orders/{order_id}", headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            return data.get("id") == order_id
        except httpx.HTTPStatusError as e:
            print(f"Order check failed: {e}")
            return False