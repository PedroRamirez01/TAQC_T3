import pytest
from config.config import Config
from utils.api_requests import get_user_by_email

# Total pruebas: 7
# Pruba 1: Registro exitoso
# Prueba 2: Registro con 'First name' vacío
# Prueba 3: Registro con 'Last name' vacío
# Prueba 4: Registro con 'Email' vacío
# Prueba 5: Registro con 'Password' vacío
# Prueba 6: Registro con 'Email' inválido
# Prueba 7: Registro con 'Email' existente

@pytest.mark.asyncio
async def test_successful_registration(register_page, delete_user):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    user = get_user_by_email(Config.USER_EMAIL)
    assert user["email"] == Config.USER_EMAIL

# Forma 1
@pytest.mark.asyncio
async def test_registration_with_empty_first_name(register_page):
    await register_page.register(
        "",
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    try:
        user = get_user_by_email(Config.USER_EMAIL)
        assert False, "'First name' vacío"
    except KeyError:
        pass

# Forma 2
# @pytest.mark.asyncio
# async def test_registration_with_empty_first_name(register_page):
#     await register_page.register(
#         "",
#         Config.USER_LAST_NAME,
#         Config.USER_EMAIL,
#         Config.USER_PASSWORD
#         )
#     assert await register_page.get_field_validation_state("firstName") is True

@pytest.mark.asyncio
async def test_registration_with_empty_last_name(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        "",
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    try:
        user = get_user_by_email(Config.USER_EMAIL)
        assert False, "'Last name' vacío"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_registration_with_empty_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        "",
        Config.USER_PASSWORD
        )
    try:
        user = get_user_by_email(Config.USER_EMAIL)
        assert False, "'Email' vacío"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_registration_with_empty_password(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        ""
        )
    try:
        user = get_user_by_email(Config.USER_EMAIL)
        assert False, "'Password' vacío"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_registration_with_invalid_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_INVALID_EMAIL,
        Config.USER_PASSWORD
        )
    try:
        user = get_user_by_email(Config.USER_EMAIL)
        assert False, "Email ingresado no es válido"
    except KeyError:
        pass

@pytest.mark.asyncio
async def test_registration_whit_existing_email(register_page):
    try:
        user = get_user_by_email(Config.USER_EMAIL)
        assert False, "Email ya existe"
    except KeyError:
        pass
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.OLD_USER_EMAIL,
        Config.USER_PASSWORD
        )