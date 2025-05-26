import pytest
from playwright.async_api import Page
from pages.login_page import LoginPage
from models.login_user import LoginUser
from utils.login_data import login_valid_users, login_no_register_users, login_user_invalid_email, login_user_empty_email, login_user_empty_password

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_valid_users)
async def test_login_successful(page: Page, user: LoginUser):
    """Test for successful login."""
    login_page = LoginPage(page)
    await login_page.login(user)
    assert "/my-account" in login_page.page.url, f"The login was not successful: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_no_register_users)
async def test_login_no_register_user(page: Page, user: LoginUser):
    """Test for login with unregistered user."""
    login_page = LoginPage(page)
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"You logged in with invalid credentials: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_user_invalid_email)
async def test_login_invalid_email(page: Page, user: LoginUser):
    """Test for login with invalid email."""
    login_page = LoginPage(page)
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"You logged in with an invalid email address: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_user_empty_email)
async def test_login_empty_email(page: Page, user: LoginUser):
    """Test for login with empty email."""
    login_page = LoginPage(page)
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"Logged in with empty email: {user}."

@pytest.mark.asyncio
@pytest.mark.parametrize("user", login_user_empty_password)
async def test_login_empty_password(page: Page, user: LoginUser):
    """Test for login with empty password."""
    login_page = LoginPage(page)
    await login_page.login(user)
    assert "/login" in login_page.page.url, f"Login with empty password: {user}."