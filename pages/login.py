from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def login(self, email: str, password: str):
        await self.page.fill("#loginEmail", email)
        await self.page.fill("#loginPassword", password)
        await self.page.click("#login > div > form > div:nth-child(4) > button")
