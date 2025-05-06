import pytest
from playwright.async_api import Page
from models.register_user import RegisterUser
from utils.register_data import register_valid_users, register_empty_field_firstname, register_empty_field_lastname, register_empty_field_email, register_empty_field_password, register_invalid_email_users, register_invalid_password_users, register_invalid_firstname_users, register_invalid_lastname_users, register_user_already_create

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_valid_users],
    indirect=["auto_delete_user"]
)
async def test_successful_registration(register_page: Page, user: RegisterUser, auto_delete_user):
    """Verify that registration is successful and redirects to the login page."""
    await register_page.register(user)
    assert "/login" in register_page.page.url, f"Valid user not created: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_empty_field_firstname],
    indirect=["auto_delete_user"]
)
async def test_registration_with_empty_field_firstname(register_page: Page, auto_delete_user, user: RegisterUser):
    """Registration with empty first name: Verify that registration fails if the first name is empty"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with empty field firstname: '{user.first_name}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_empty_field_lastname],
    indirect=["auto_delete_user"]
)
async def test_registration_with_empty_field_lastname(register_page: Page, auto_delete_user, user: RegisterUser):
    """Registration with empty last name: Verify that registration fails if the last name is empty"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with empty field lastname: '{user.last_name}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_empty_field_email],
    indirect=["auto_delete_user"]
)
async def test_registration_with_empty_field_email(register_page: Page, auto_delete_user, user: RegisterUser):
    """Registration with empty email: Verify that registration fails if the email is empty"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with empty field email: '{user.email}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_empty_field_password],
    indirect=["auto_delete_user"]
)
async def test_registration_with_empty_field_password(register_page: Page, auto_delete_user, user: RegisterUser):
    """Registration with empty password: Verify that registration fails if the password is empty"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with empty field password: '{user.password}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_firstname_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_firstname(register_page: Page, user: RegisterUser, auto_delete_user):
    """Registration with invalid first name: Verify that registration fails if the first name is invalid"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid firstname: '{user.first_name}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_lastname_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_lastname(register_page: Page, user: RegisterUser, auto_delete_user):
    """Registration with invalid last name: Verify that registration fails if the last name is invalid"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid lastname: '{user.last_name}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_email_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_email(register_page: Page, user: RegisterUser, auto_delete_user):
    """Registration with invalid email: Verify that registration fails if the email is invalid"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid email address: '{user.email}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_invalid_password_users],
    indirect=["auto_delete_user"]
)
async def test_registration_with_invalid_password_security(register_page: Page, user: RegisterUser, auto_delete_user):
    """Registration with invalid password: Verify that registration fails if the password does not meet the security requirements"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an invalid password security: '{user.password}'."

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user, auto_delete_user",
    [(user, user) for user in register_user_already_create],
    indirect=["auto_delete_user"]
)
async def test_registration_with_user_already_create(register_page: Page, user: RegisterUser, auto_delete_user):
    """Registration with already registered user: Verify that registration fails if the user is already registered"""
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"A user was created with an already registered email: '{user.email}'."
