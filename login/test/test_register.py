import pytest
import requests
from config.config import Config
from utils.api_requests import get_user_by_email

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
        assert False, "El registro no debería haber sido exitoso con el primer nombre vacío"
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

# @pytest.mark.asyncio
# async def test_registration_with_empty_last_name(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         "",
#         Config.USER_EMAIL,
#         Config.USER_PASSWORD
#         )
#     assert await register_page.get_field_validation_state("lastName") is True

# @pytest.mark.asyncio
# async def test_registration_with_empty_email(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         "",
#         Config.USER_PASSWORD
#         )
#     assert await register_page.get_field_validation_state("email") is True

# @pytest.mark.asyncio
# async def test_registration_with_empty_password(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.USER_EMAIL,
#         ""
#         )
#     assert await register_page.get_field_validation_state("password") is True

# @pytest.mark.asyncio
# async def test_registration_with_invalid_email(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.INVALID_EMAIL,
#         Config.USER_PASSWORD
#         )
#     assert await register_page.get_field_validation_state("email") is True

# @pytest.mark.asyncio
# async def test_registration_whit__existing_email(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.USER_EMAIL,
#         Config.USER_PASSWORD
#         )
#     assert "/register" in register_page.page.url