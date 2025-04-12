from playwright.async_api import Page
from models.login_user import LoginUser

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.field_email = page.locator("#loginEmail")
        self.field_password = page.locator("#loginPassword")
        self.btn_login = page.locator("#login > div > form > div:nth-child(4) > button")

    async def navigate(self, url: str) -> None:
        await self.page.goto(url, wait_until="domcontentloaded")

    async def fill_email(self, email: str) -> None:
        await self.field_email.fill(email)

    async def fill_password(self, password: str) -> None:
        await self.field_password.fill(password)

    async def submit(self) -> None:
        await self.btn_login.click()

    async def login(self, user: LoginUser) -> None:
        await self.fill_email(user.email)
        await self.fill_password(user.password)
        await self.submit()
        await self.page.wait_for_timeout(2000)
