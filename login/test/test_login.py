# import pytest
# from config.config import Config

# @pytest.mark.asyncio
# async def test_successful_login(login_page):
#     await login_page.login(Config.USER_EMAIL, Config.USER_PASSWORD)
#     assert await "/my-account" in login_page.page.url

# @pytest.mark.asyncio
# async def test_login_with_empty_email(login_page):
#     await login_page.login("", Config.USER_PASSWORD)
#     assert await login_page.get_field_validation_state("email") is True

# @pytest.mark.asyncio
# async def test_login_with_empty_password(login_page):
#     await login_page.login(Config.USER_EMAIL, "")
#     assert await login_page.get_field_validation_state("password") is True

# @pytest.mark.asyncio
# async def test_login_with_invalid_credentials(login_page):
#     await login_page.login(Config.INVALID_EMAIL, Config.INVALID_PASSWORD)
#     assert await "/login" in login_page.page.url