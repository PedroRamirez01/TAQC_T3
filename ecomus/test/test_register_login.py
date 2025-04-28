import pytest
from playwright.async_api import Page
from models.register_login_users import RegisterLoginUser
from utils.users_data import register_login_valid_new_users, register_login_invalid_new_users

"""_summary_
The following tests were performed:
    1. Registration and login success: Verifies that registration is successful 
        and redirects to the login page, followed by a successful login.
    2. Registration and login with empty or invalid fields: Verifies that
        registration fails if there are empty or invalid fields, and that login
        is not successful with these credentials.
"""

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user.login) for user in register_login_valid_new_users],
    indirect=["auto_delete_user"]
)
async def test_successful_registration_login_valid(register_page: Page, login_page: Page, user: RegisterLoginUser, auto_delete_user):
    await register_page.register(user.register)
    assert "/login" in register_page.page.url, f"Valid user not created: {user.register}."
    await login_page.login(user.login)
    assert "/my-account" in login_page.page.url, f"The login was not successful: {user.login}."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user.login) for user in register_login_invalid_new_users],
    indirect=["auto_delete_user"]
)
async def test_successful_registration_login_invalid(register_page: Page, login_page: Page, user: RegisterLoginUser, auto_delete_user):
    await register_page.register(user.register)
    await login_page.login(user.login)
    assert "/my-account" in login_page.page.url, f"You logged in with invalid credentials: {user.register}."
