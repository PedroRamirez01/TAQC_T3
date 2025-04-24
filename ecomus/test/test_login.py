import pytest
from playwright.async_api import Page
from models.login_user import LoginUser
from utils.users_data import login_valid_users, login_no_register_users, login_user_invalid_email, login_user_empty_email, login_user_empty_password

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_valid_users)
async def test_login_successful(login_page: Page, user: LoginUser):
    """
    Se prueba el login con credenciales válidas.
    """
    await login_page.login(user)
    assert "/my-account" in login_page.page.url, f"El inicio de sesión no fue exitoso: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_no_register_users)
async def test_login_no_register_user(login_page: Page, user: LoginUser):
    """
    Se prueba el login con credenciales de usuario no registrado.
    """
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"Se inició sesión con credenciales inválidas: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_user_invalid_email)
async def test_login_invalid_email(login_page: Page, user: LoginUser):
    """
    Se prueba el login con email inválido.
    """
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"Se inició sesión con email inválido: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_user_empty_email)
async def test_login_empty_email(login_page: Page, user: LoginUser):
    """
    Se prueba el login con email vacío.
    """
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"Se inició sesión con email vacío: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_user_empty_password)
async def test_login_empty_email(login_page: Page, user: LoginUser):
    """
    Se prueba el login con password vacío.
    """
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"Se inició sesión con password vacía: {user}"