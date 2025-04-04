import pytest_asyncio
from playwright.async_api import async_playwright
from config.config import Config
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

@pytest_asyncio.fixture(scope="function")
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        yield page
        await browser.close()

@pytest_asyncio.fixture
async def login_page(page):
    login_page = LoginPage(page)
    await login_page.navigate(Config.URL_LOGIN_PAGE)
    return login_page

@pytest_asyncio.fixture
async def register_page(page):
    register_page = RegisterPage(page)
    await register_page.navigate(Config.URL_REGISTER_PAGE)
    return register_page