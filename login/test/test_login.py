import pytest
from config.config import Config

@pytest.mark.asyncio
async def test_successful_login(login_page):
    await login_page.login(Config.EMAIL, Config.PASSWORD)
    # Verifica que el usuario sea redirigido al dashboard después de un login exitoso
    assert "/dashboard" in login_page.page.url

@pytest.mark.asyncio
async def test_login_with_empty_email(login_page):
    await login_page.login("", Config.PASSWORD)
    # Verifica que se muestre un mensaje de error si el email está vacío
    error_message = await login_page.get_error_message()
    assert "Email is required" in error_message

@pytest.mark.asyncio
async def test_login_with_empty_password(login_page):
    await login_page.login(Config.EMAIL, "")
    # Verifica que se muestre un mensaje de error si la contraseña está vacía
    error_message = await login_page.get_error_message()
    assert "Password is required" in error_message

@pytest.mark.asyncio
async def test_login_with_invalid_credentials(login_page):
    await login_page.login("invalid@example.com", "wrongpassword")
    # Verifica que se muestre un mensaje de error si las credenciales son incorrectas
    error_message = await login_page.get_error_message()
    assert "Invalid credentials" in error_message