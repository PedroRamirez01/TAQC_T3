from playwright.async_api import Page

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

    async def register(self, firstName: str, lastName: str, email: str, password: str):
        await self.page.fill("input[name='firstName']", firstName)
        await self.page.fill("input[name='lastName']", lastName)
        await self.page.fill("input[name='email']", email)
        await self.page.fill("input[name='password']", password)
        await self.page.click("button[type=submit]")
