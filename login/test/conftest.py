import pytest_asyncio
from playwright.async_api import Page
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.product_detail_page import ProductDetailPage
from utils.api_requests import delete_user_by_id

@pytest_asyncio.fixture(scope="function")
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        yield page
        await browser.close()

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