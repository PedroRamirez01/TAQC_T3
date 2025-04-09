import dotenv
import os

class Config:
    dotenv.load_dotenv()
    URL_REGISTER_PAGE = "https://automation-portal-bootcamp.vercel.app/register"
    URL_LOGIN_PAGE = "https://automation-portal-bootcamp.vercel.app/login"

    OLD_USER_EMAIL = os.getenv("OLD_USER_EMAIL")
    OLD_USER_PASSWORD = os.getenv("OLD_USER_PASSWORD")
    
    USER_FIRST_NAME = os.getenv("USER_FIRST_NAME")
    USER_LAST_NAME = os.getenv("USER_LAST_NAME")
    USER_EMAIL = os.getenv("USER_EMAIL")
    USER_PASSWORD = os.getenv("USER_PASSWORD")

    USER_INVALID_EMAIL = os.getenv("USER_INVALID_EMAIL")
    USER_INVALID_PASSWORD = os.getenv("USER_INVALID_PASSWORD")

    NOT_REGISTERED_EMAIL = os.getenv("NOT_REGISTERED_EMAIL")
    NOT_REGISTERED_PASSWORD = os.getenv("NOT_REGISTERED_PASSWORD")
