import pytest_asyncio
from playwright.async_api import async_playwright
from config.config import Config
from pages.homePage_page import HomeToPage
from pages.filter_product_page import FilterProductPage

@pytest_asyncio.fixture(scope="function") # Inicializa el navegador y la página para cada prueba 
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        yield page # Proporciona la página a las pruebas
        await browser.close()

@pytest_asyncio.fixture
async def homeTo_page(page):
    home_page = HomeToPage(page)
    await home_page.navigate(Config.URL_BASE)
    return home_page

@pytest_asyncio.fixture
async def filter_page(page):
    filter_page = FilterProductPage(page)
    await filter_page.navigate(Config.URL_FILTER)
    return filter_page