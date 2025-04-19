from dotenv import load_dotenv
import os

class Config:
    load_dotenv()
    URL_BASE = "https://automation-portal-bootcamp.vercel.app/"
    URL_FILTER = "https://automation-portal-bootcamp.vercel.app/shop-default"
    MAX_ATTEMPTS = 1
    DELAY = 1000