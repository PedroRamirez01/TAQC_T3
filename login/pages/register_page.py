from playwright.async_api import Page
import models.register_user as RegisterUser

class RegisterPage:
    def __init__(self, page: Page, URL: str):
        self.URL = URL
        self.page = page
        self.fieldFirstName = self.page.locator("#register-form > div:nth-child(1) > input")
        self.fieldLastName = self.page.locator("input[name='lastName']")
        self.fieldEmail = self.page.locator("input[name='email'][placeholder=' ']")
        self.fieldPassword = self.page.locator("input[name='password']")
        self.btnRegister = self.page.locator("#register-form > div.mb_20 > button")

    async def navigate(self, URL: str) -> None:
        await self.page.goto(URL, wait_until="domcontentloaded")

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
        await self.navigate(self.URL)
        await self.fill_first_name(user.first_name)
        await self.fill_last_name(user.last_name)
        await self.fill_email(user.email)
        await self.fill_password(user.password)
        await self.submit()
        await self.page.wait_for_timeout(3000)
