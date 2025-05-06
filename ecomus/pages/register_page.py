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
        """
        Navigates to the registration page.
        This method is called before filling in the registration form.
        It ensures that the page is loaded and ready for interaction.
        """
        await self.page.goto(self.url, wait_until="domcontentloaded")

    async def fill_first_name(self, firstName: str) -> None:
        """
        Fills the first name field.
        Args:
            firstName (str): The first name to fill in.
        """
        await self.fieldFirstName.wait_for(state="visible")
        await self.fieldFirstName.fill(firstName)

    async def fill_last_name(self, lastName: str) -> None:
        """
        Fills the last name field.
        Args:
            lastName (str): The last name to fill in.
        """
        await self.fieldLastName.wait_for(state="visible")
        await self.fieldLastName.fill(lastName)

    async def fill_email(self, email: str) -> None:
        """
        Fills in the email field.
        Args:
            email (str): The email to fill in.
        """
        await self.fieldEmail.wait_for(state="visible")
        await self.fieldEmail.fill(email)
    
    async def fill_password(self, password: str) -> None:
        """
        Fills in the password field.
        Args:
            password (str): The password to fill in.
        """
        await self.fieldPassword.wait_for(state="visible")
        await self.fieldPassword.fill(password)

    async def submit(self) -> None:
        """
        Clicks the registration button.
        This method is called after filling in the registration form.
        It submits the form and initiates the registration process.
        """
        await self.btnRegister.wait_for(state="visible")
        await self.btnRegister.click()

    async def register(self, user: RegisterUser) -> None:
        """
        Registers the user using the provided data.
        This method combines all the steps of navigating to the page, filling in the form, and submitting it.
        Args:
            user (RegisterUser): The user data to register.
        """
        await self.navigate()
        await self.fill_first_name(user.first_name)
        await self.fill_last_name(user.last_name)
        await self.fill_email(user.email)
        await self.fill_password(user.password)
        await self.submit()
        await self.page.wait_for_timeout(3000)
