import pytest
from config.config import Config

@pytest.mark.asyncio
async def test_successful_registration(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    assert "/my-account" in register_page.page.url

@pytest.mark.asyncio
async def test_registration_with_empty_first_name(register_page):
    await register_page.register(
        "",
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    assert await register_page.get_field_validation_state("firstName") is True

@pytest.mark.asyncio
async def test_registration_with_empty_last_name(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        "",
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    assert await register_page.get_field_validation_state("lastName") is True

@pytest.mark.asyncio
async def test_registration_with_empty_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        "",
        Config.USER_PASSWORD
        )
    assert await register_page.get_field_validation_state("email") is True

@pytest.mark.asyncio
async def test_registration_with_empty_password(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        ""
        )
    assert await register_page.get_field_validation_state("password") is True

@pytest.mark.asyncio
async def test_registration_with_invalid_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.INVALID_EMAIL,
        Config.USER_PASSWORD
        )
    assert await register_page.get_field_validation_state("email") is True

@pytest.mark.asyncio
async def test_registration_whit__existing_email(register_page):
    await register_page.register(
        Config.USER_FIRST_NAME,
        Config.USER_LAST_NAME,
        Config.USER_EMAIL,
        Config.USER_PASSWORD
        )
    assert "/register" in register_page.page.url