import requests
import os

TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_user_by_email(email):
    response = requests.get(f"{BASE_URL}api/user?email={email}", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def delete_user_by_id(user_id):
    url = f"{BASE_URL}api/user/{user_id}"
    try:
        response = requests.delete(url, headers=HEADERS)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error al eliminar usuario: {e}")
        return None