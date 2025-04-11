import pytest_asyncio
from playwright.async_api import async_playwright
from config.config import Config
from pages.search_page import HomeToSearchPage
from pages.filter_product_page import FilterProductPage

@pytest_asyncio.fixture(scope="function") # Inicializa el navegador y la página para cada prueba 
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        yield page # Proporciona la página a las pruebas
        await browser.close()

@pytest_asyncio.fixture
async def search_page(page):
    search_page = HomeToSearchPage(page)
    await search_page.navigate(Config.URL)
    return search_page

@pytest_asyncio.fixture
async def filter_page(page):
    filter_page = FilterProductPage(page)
    await filter_page.navigate(Config.URL)
    return filter_page