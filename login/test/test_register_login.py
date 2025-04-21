import pytest
from playwright.async_api import Page
from models.register_login_users import RegisterLoginUser
from utils.users_data import register_login_valid_new_users, register_login_invalid_new_users

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user.login) for user in register_login_valid_new_users],
    indirect=["auto_delete_user"]
)
async def test_successful_registration_login_valid(register_page: Page, login_page: Page, user: RegisterLoginUser, auto_delete_user):
    await register_page.register(user.register)
    assert "/login" in register_page.page.url, f"Usuario valido no creado: {user.register}"
    await login_page.login(user.login)
    assert "/my-account" in login_page.page.url, f"El inicio de sesión no fue exitoso: {user.login}"

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user.login) for user in register_login_invalid_new_users],
    indirect=["auto_delete_user"]
)
async def test_successful_registration_login_invalid(register_page: Page, login_page: Page, user: RegisterLoginUser, auto_delete_user):
    await register_page.register(user.register)
    # assert "/login" in register_page.page.url, f"Usuario invalido creado: {user.register}"
    await login_page.login(user.login)
    assert "/my-account" in login_page.page.url, f"Se inició sesión con credenciales inválidas: {user.register}"
