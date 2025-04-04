import pytest_asyncio
from playwright.async_api import async_playwright
from config.config import Config
from pages.login_page import LoginPage

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