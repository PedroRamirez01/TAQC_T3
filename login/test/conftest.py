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

@pytest.fixture(autouse=False, scope="function")
async def limpiar_usuario_al_final():
    yield
    email = Config.USER_EMAIL
    print(email)
    try:
        user = get_user_by_email(email)
        if user and "id" in user:
            status = delete_user_by_id(user["id"])
            if status in [200, 204]:
                print(f"[Teardown] Usuario {email} eliminado.")
            else:
                print(f"[Teardown] Falló la eliminación. Status: {status}")
        else:
            print(f"[Teardown] Usuario {email} no existe, no se eliminó nada.")
    except Exception as e:
        print(f"[Teardown] Error al eliminar usuario: {e}")

@pytest_asyncio.fixture
async def register_page(page):
    register_page = RegisterPage(page)
    await register_page.navigate(Config.URL_REGISTER_PAGE)
    return register_page

@pytest_asyncio.fixture
async def login_page(page):
    login_page = LoginPage(page)
    await login_page.navigate(Config.URL_LOGIN_PAGE)
    return login_page