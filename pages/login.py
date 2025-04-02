from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.fieldEmail = self.page.locator("#loginEmail")
        self.fieldPassword = self.page.locator("#loginPassword")
        self.btnLogin = self.page.locator("#login > div > form > div:nth-child(4) > button")

    async def loginEmail(self, email: str):
        assert email, "Email is empty"
        await self.page.fill("#loginEmail", email)

    async def loginPassword(self, password: str):
        assert password, "Password is empty"
        await self.page.fill("#loginPassword", password)

    async def pressBtnLogin(self):
        assert self.btnLogin, "Button Login is not found"
        await self.btnLogin.click()
