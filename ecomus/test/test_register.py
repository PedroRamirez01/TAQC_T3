import pytest
from playwright.async_api import Page
from models.register_user import RegisterUser
from utils.users_data import register_valid_users, register_empty_fields_users, register_invalid_email_users, register_invalid_password_users, register_invalid_firstname_users, register_invalid_lastname_users

"""_summary_
The following tests were performed:
    1. Verify that registration is successful and redirects to the login page.
    2. Registration with empty fields: Verify that registration fails if there are empty fields.
    3. Registration with invalid first name: Verify that registration fails if the first name is invalid.
    4. Registration with invalid last name: Verify that registration fails if the last name is invalid.
    5. Registration with invalid email: Verify that registration fails if the email is invalid.
    6. Registration with invalid password: Verify that registration fails if the password does not meet the security requirements.
"""

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_valid_users],
    indirect=["auto_delete_user"]
)
async def test_successful_registration(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/login" in register_page.page.url, f"Valid user not created: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_empty_fields_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_empty_fields(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with 1 or more empty fields: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_firstname_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_firstname(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid firstname: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_lastname_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_lastname(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid lastname: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_email_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_email(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid email address: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_password_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_password_security(register_page: Page, user: RegisterUser, auto_delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid password: {user}."