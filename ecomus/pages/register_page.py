from playwright.async_api import Page
import models.register_user as RegisterUser
from config.config import Config

class RegisterPage:
    """_summary_
    Class that represents the registration page on the test website.
    Provides methods for interacting with page elements and registering a new user.
    Attributes:
        url (str): URL of the registration page.
        page (Page): Instance of the Playwright page.
        fieldFirstName (Locator): Locator for the first name field.
        fieldLastName (Locator): Locator for the last name field.
        fieldEmail (Locator): Locator for the email field.
        fieldPassword (Locator): Locator for the password field.
        btnRegister (Locator): Locator for the registration button.
    Methods:
        navigate(): Navigates to the registration page.
        fill_first_name(firstName: str): Fills the first name field.
        fill_last_name(lastName: str): Fills the last name field.
        fill_email(email: str): Fills in the email field.
        fill_password(password: str): Fills in the password field.
        submit(): Clicks the registration button.
        register(user: RegisterUser): Registers the user using the provided data.
    """

    def __init__(self, page: Page) -> None:
        self.url = Config.URL_REGISTER_PAGE
        self.page = page
        self.fieldFirstName = self.page.locator("#register-form > div:nth-child(1) > input")
        self.fieldLastName = self.page.locator("input[name='lastName']")
        self.fieldEmail = self.page.locator("input[name='email'][placeholder=' ']")
        self.fieldPassword = self.page.locator("input[name='password']")
        self.btnRegister = self.page.locator("#register-form > div.mb_20 > button")

    async def navigate(self) -> None:
        await self.page.goto(self.url, wait_until="domcontentloaded")

    async def fill_first_name(self, firstName: str) -> None:
        await self.fieldFirstName.wait_for(state="visible")
        await self.page.screenshot(path="error_msg_register.png", full_page=True)
        await self.fieldFirstName.fill(firstName)

    async def fill_last_name(self, lastName: str) -> None:
        await self.fieldLastName.fill(lastName)

    async def fill_email(self, email: str) -> None:
        await self.fieldEmail.fill(email)
    
    async def fill_password(self, password: str) -> None:
        await self.fieldPassword.fill(password)

    async def submit(self) -> None:
        await self.btnRegister.click()

    async def register(self, user: RegisterUser) -> None:
        await self.navigate()
        await self.fill_first_name(user.first_name)
        await self.fill_last_name(user.last_name)
        await self.fill_email(user.email)
        await self.fill_password(user.password)
        await self.submit()
        await self.page.wait_for_timeout(3000)
