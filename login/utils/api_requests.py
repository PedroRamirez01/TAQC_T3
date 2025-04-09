import requests
import os

TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_user_by_email(email):
    try:
        response = requests.get(f"{BASE_URL}api/user?email={email}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return None
        raise

def delete_user_by_id(email):
    try:
        user = get_user_by_email(email)
        response = requests.delete(f"{BASE_URL}api/user/{user["id"]}", headers=HEADERS)
        return response.status_code
    except requests.RequestException as e:
        return None