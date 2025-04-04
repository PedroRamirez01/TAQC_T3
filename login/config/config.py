from dotenv import load_dotenv
import os

class Config:
    load_dotenv()
    # Login settings
    URL_LOGIN_PAGE = "https://automation-portal-bootcamp.vercel.app/login"
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    INVALID_EMAIL = os.getenv("INVALID_EMAIL")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")
    # Registration details
    URL_REGISTER_PAGE = "https://automation-portal-bootcamp.vercel.app/register"
    NEW_USER_FIRST_NAME = os.getenv("NEW_USER_FIRST_NAME")
    NEW_USER_LAST_NAME = os.getenv("NEW_USER_LAST_NAME")
    NEW_USER_EMAIL = os.getenv("NEW_USER_EMAIL")
    NEW_USER_PASSWORD = os.getenv("NEW_USER_PASSWORD")
