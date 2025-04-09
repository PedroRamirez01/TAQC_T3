import pytest
from config.config import Config
from utils.api_requests import get_user_by_email

# Total pruebas: 7
# Pruba 1: Login exitoso
# Prueba 2: Login con credenciales inválidas
# Prueba 3: Login con email no registrado
# Prueba 4: Login con email inválido
# Prueba 5: Login con email vacío
# Prueba 6: Login con password vacío

@pytest.mark.asyncio
async def test_successful_login(login_page):
    try:
        user = get_user_by_email(Config.OLD_USER_EMAIL)
        await login_page.login(Config.OLD_USER_EMAIL, Config.OLD_USER_PASSWORD)
        assert "/my-account" in login_page.page.url, "El inicio de sesión no fue exitoso"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_login_with_invalid_credentials(login_page):
    try:
        user = get_user_by_email(Config.USER_INVALID_EMAIL)
        await login_page.login(Config.USER_INVALID_EMAIL, Config.USER_INVALID_PASSWORD)
        assert "/login" in login_page.page.url, "Credenciales inválidas"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_login_whit_email_not_valid(login_page):
    try:
        user = get_user_by_email(Config.USER_INVALID_EMAIL)
        await login_page.login(Config.USER_INVALID_EMAIL, Config.USER_INVALID_PASSWORD)
        assert "/login" in login_page.page.url, "Email inválido"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_login_whit_email_not_registered(login_page):
    try:
        user = get_user_by_email(Config.NOT_REGISTERED_EMAIL)
        await login_page.login(Config.NOT_REGISTERED_EMAIL, Config.NOT_REGISTERED_PASSWORD)
        assert "/login" in login_page.page.url, "Email no registrado"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_login_with_empty_email(login_page):
    try:
        user = get_user_by_email(Config.OLD_USER_PASSWORD)
        await login_page.login("", Config.OLD_USER_PASSWORD)
        assert "/login" in login_page.page.url, "Email no ingresado"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_login_with_empty_password(login_page):
    try:
        user = get_user_by_email(Config.OLD_USER_EMAIL)
        await login_page.login(Config.OLD_USER_EMAIL, "")
        assert "/login" in login_page.page.url, "Contraseña no ingresada"
    except KeyError:
        pass