import pytest_asyncio
from playwright.async_api import async_playwright
from config.config import Config
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.api_requests import get_user_by_email, delete_user_by_id
import pytest

@pytest_asyncio.fixture(scope="function")
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        yield page
        await browser.close()

@pytest_asyncio.fixture
async def register_page(page):
    register_page = RegisterPage(page)
    await register_page.navigate(Config.URL_REGISTER_PAGE)
    return register_page

@pytest.fixture(scope="function")
def delete_user(request):
    # Elimina al usuario después de cada prueba
    def _delete_user():
        delete_user_by_id(Config.USER_EMAIL)
    request.addfinalizer(_delete_user)

# @pytest_asyncio.fixture
# async def login_page(page):
#     login_page = LoginPage(page)
#     await login_page.navigate(Config.URL_LOGIN_PAGE)
#     return login_page