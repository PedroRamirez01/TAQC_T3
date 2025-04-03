from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.field_email = page.locator("#loginEmail")
        self.field_password = page.locator("#loginPassword")
        self.btn_login = page.locator("#login > div > form > div:nth-child(4) > button")
        self.error_message = page.locator(".error-message")

    async def navigate(self, url: str):
        await self.page.goto(url, wait_until="domcontentloaded")

    async def fill_email(self, email: str):
        await self.field_email.fill(email)

    async def fill_password(self, password: str):
        await self.field_password.fill(password)

    async def submit(self):
        await self.btn_login.click()

    async def login(self, email: str, password: str):
        await self.fill_email(email)
        await self.fill_password(password)
        await self.submit()

    async def get_error_message(self) -> str:
        return await self.error_message.inner_text()
