import pytest_asyncio
from playwright.async_api import Page
from playwright.async_api import async_playwright
from pages.checkout_page import CheckoutPage
from pages.home_page import HomeToPage
from pages.filterProduct_page import FilterProductPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.product_detail_page import ProductDetailPage
from utils.api_requests import delete_user_by_id
from config.config import Config

@pytest_asyncio.fixture(scope="function")
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=100)
        page = await browser.new_page()
        yield page
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

@pytest_asyncio.fixture
async def register_page(page: Page):
    register_page = RegisterPage(page)
    return register_page

@pytest_asyncio.fixture
async def login_page(page: Page):
    login_page = LoginPage(page)
    return login_page

@pytest_asyncio.fixture
async def register_login_page(page: Page):
    register_page = RegisterPage(page)
    login_page = LoginPage(page)
    return register_page, login_page

@pytest_asyncio.fixture
async def product_detail_page(page: Page):
    product_detail = ProductDetailPage(page)
    return product_detail

@pytest_asyncio.fixture
async def auto_delete_user(request):
    user = request.param
    email = user.email
    yield
    await delete_user_by_id(email)

@pytest_asyncio.fixture
async def auto_delete_user_e2e(request):
    user = request.param
    email = user["email"]
    yield
    await delete_user_by_id(email)

@pytest_asyncio.fixture
async def checkout_page(page: Page):
    await page.goto(Config.URL_BASE)
    return CheckoutPage(page)
