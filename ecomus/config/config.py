import dotenv

class Config:
    dotenv.load_dotenv()
    URL_REGISTER_PAGE = "https://automation-portal-bootcamp.vercel.app/register"
    URL_LOGIN_PAGE = "https://automation-portal-bootcamp.vercel.app/login"
    URL_PRODUCT_DETAIL_PAGE = "https://automation-portal-bootcamp.vercel.app/product-detail/453"
    URL_BASE = "https://automation-portal-bootcamp.vercel.app/"
    URL_FILTER = "https://automation-portal-bootcamp.vercel.app/shop-default"
    MAX_ATTEMPTS = 1
    DELAY = 1000
