import pytest
from playwright.async_api import Page
from models.register_user import RegisterUser
from utils.users_data import register_valid_users, register_empty_fields_users, register_invalid_email_users, register_invalid_password_users, register_invalid_firstname_users, register_invalid_lastname_users

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_valid_users],
    indirect=["auto_delete_user"]
)
async def test_successful_registration(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/login" in register_page.page.url, f"Usuario valido no creado: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_empty_fields_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_empty_fields(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"Se creó un usuario con 1 o más campos vacíos: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_firstname_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_firstname(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"Se creó un usuario con un firstname inválido: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_lastname_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_lastname(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"Se creó un usuario con un lastname inválido: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_email_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_email(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"Se creó un usuario con un email inválido: {user}"

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_password_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_password_security(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"Se creó un usuario con una contraseña inválida: {user}"