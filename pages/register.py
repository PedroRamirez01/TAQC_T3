from playwright.async_api import Page

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.fieldFirstName = self.page.locator("input[name='firstName']")
        self.fieldLastName = self.page.locator("input[name='lastName']")
        self.fieldEmail = self.page.locator("input[name='email'][placeholder=' ']")
        self.fieldPassword = self.page.locator("input[name='password']")
        self.btnRegister = self.page.locator("#register-form > div.mb_20 > button")

    async def registerFirstName(self, firstName: str) -> None:
        assert firstName, "First name is empty"
        await self.fieldFirstName.fill(firstName)

    async def registerLastName(self, lastName: str) -> None:
        assert lastName, "Last name is empty"
        await self.fieldLastName.fill(lastName)

    async def registerEmail(self, email: str) -> None:
        assert email, "Email is empty"
        await self.fieldEmail.fill(email)
    
    async def registerPassword(self, password: str) -> None:
        assert password, "Password is empty"
        await self.fieldPassword.fill(password)
    
    async def pressBtnRegister(self) -> None:
        assert self.btnRegister, "Button Register is not found"
        await self.btnRegister.click()
