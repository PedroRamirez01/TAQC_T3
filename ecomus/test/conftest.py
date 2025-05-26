import pytest_asyncio
from playwright.async_api import async_playwright
from utils.api_requests import delete_user_by_id

@pytest_asyncio.fixture(scope="function")
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        yield page
        await browser.close()

@pytest_asyncio.fixture
async def auto_delete_user(request):
    user = request.param
    email = user.email
    yield
    await delete_user_by_id(email)

@pytest_asyncio.fixture
async def auto_delete_user_e2e(request):
    email = request.param["email"]
    yield
    await delete_user_by_id(email)