from playwright.async_api import Page

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

    async def login(self, email: str, password: str) -> None:
        await self.fill_email(email)
        await self.fill_password(password)
        await self.submit()
        await self.page.wait_for_timeout(3000)
        
    async def get_field_validation_state(self, field_name: str) -> bool:
        await self.page.screenshot(path=f"error_msg_login_{field_name}.png", full_page=True)
        return await self.page.evaluate(f"document.querySelector('#login{field_name.capitalize()}').validity.valueMissing")