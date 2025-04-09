import pytest
from config.config import Config
from utils.api_requests import get_user_by_email, delete_user_by_id

# Total pruebas: 7
# Pruba 1: Registro exitoso
# Prueba 2: Registro con 'First name' vacío
# Prueba 3: Registro con 'Last name' vacío
# Prueba 4: Registro con 'Email' vacío
# Prueba 5: Registro con 'Password' vacío
# Prueba 6: Registro con 'Email' inválido
# Prueba 7: Registro con 'Email' existente

@pytest.mark.asyncio
async def test_successful_registration(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    delete_user_by_id(Config.USER_EMAIL)
    assert "/login" in register_page.page.url, "Usuario no registrado"

@pytest.mark.asyncio
async def test_registration_with_invalid_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.NEW_USER_INVALID_EMAIL,
        Config.NEW_USER_INVALID_PASSWORD
        )
    delete_user_by_id(Config.NEW_USER_INVALID_EMAIL)
    assert "/register" in register_page.page.url, "Se creo un usuario con email inválido"

@pytest.mark.asyncio
async def test_registration_with_empty_first_name(register_page):
    await register_page.register(
        "",
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    assert "/register" in register_page.page.url, "Se creo un usuario sin email"

@pytest.mark.asyncio
async def test_registration_whit_existing_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.OLD_USER_EMAIL,
        Config.OLD_USER_PASSWORD
        )
    assert "/register" in register_page.page.url, "Se creo un usuario con email existente"

@pytest.mark.asyncio
async def test_registration_with_empty_last_name(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        "",
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    assert "/register" in register_page.page.url, "Se creo un usuario con 'Last name' vacío"

@pytest.mark.asyncio
async def test_registration_with_empty_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        "",
        Config.USER_PASSWORD
        )
    assert "/register" in register_page.page.url, "Se creo un usuario con 'email' vacío"

@pytest.mark.asyncio
async def test_registration_with_empty_password(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        ""
        )
    assert "/register" in register_page.page.url, "Se creo un usuario con 'Password' vacío"
