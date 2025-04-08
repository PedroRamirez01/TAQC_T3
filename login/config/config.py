import dotenv
import os

class Config:
    dotenv.load_dotenv()
    URL_REGISTER_PAGE = "https://automation-portal-bootcamp.vercel.app/register"
    URL_LOGIN_PAGE = "https://automation-portal-bootcamp.vercel.app/login"
    
    USER_FIRST_NAME = os.getenv("USER_FIRST_NAME")
    USER_LAST_NAME = os.getenv("USER_LAST_NAME")
    USER_EMAIL = os.getenv("USER_EMAIL")
    USER_PASSWORD = os.getenv("USER_PASSWORD")

    INVALID_EMAIL = os.getenv("INVALID_EMAIL")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")
    
