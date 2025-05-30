from playwright.async_api import Page, expect
from models.login_user import LoginUser
from config.config import Config

class LoginPage:
    """_summary_
    Class representing the login page.
    Contains methods for navigating to the page, filling in the login fields, and submitting the form.
    Attributes:
        url (str): URL of the login page.
        page (Page): Instance of the Playwright page.
        field_email (Locator): Email input field.
        field_password (Locator): Password input field.
        btn_login (Locator): Button to submit the login form.
    Methods:
        navigate(): Navigates to the login page.
        fill_email(email: str): Fills in the email field.
        fill_password(password: str): Fills in the password field.
        submit(): Submits the login form.
        login(user: LoginUser): Logs in with the given user.
    """

    def __init__(self, page: Page):
        self.url = Config.URL_LOGIN_PAGE
        self.page = page
        self.field_email = page.locator("#loginEmail")
        self.field_password = page.locator("#loginPassword")
        self.btn_login = page.locator("#login > div > form > div:nth-child(4) > button")

    async def navigate(self) -> None:
        """Navigates to the login page."""
        await self.page.goto(self.url, wait_until="domcontentloaded")
        await expect(self.page).to_have_url(self.url)

    async def fill_email(self, email: str) -> None:
        """Fills in the email field."""
        await self.field_email.fill(email)

    async def fill_password(self, password: str) -> None:
        """Fills in the password field."""
        await self.field_password.fill(password)

    async def submit(self) -> None:
        """Submits the login form."""
        await self.btn_login.click()

    async def login(self, user: LoginUser) -> None:
        """Logs in with the given user."""
        await self.navigate()
        await self.fill_email(user.email)
        await self.fill_password(user.password)
        await self.submit()
        await self.page.wait_for_timeout(2000)

    async def fill_login_form(self, user: dict) -> None:
        """
        Fills in the login form with the provided user data.
        Args:
            user (dict): A dictionary containing user data with keys 'email' and 'password'.
        """
        await self.fill_email(user["email"])
        await self.fill_password(user["password"])
        await self.submit()