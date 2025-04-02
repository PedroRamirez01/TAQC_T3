import time
from playwright.async_api import Page

class HomeToRegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHomePage = self.page.locator("#newsletterPopup > div > div > div.modal-top > span")
        self.btnLogin = self.page.locator("#header > div > div > div.col-xxl-5.col-md-4.col-3 > ul > li.nav-account > a")
        self.linkRegister = self.page.locator("#login > div > div > div.tf-login-form > form > div.bottom > div:nth-child(2) > a")
        self.btnRegister = self.page.locator("#register > div > div > div.tf-login-form > form > div.bottom > div:nth-child(1) > a")
        self.popUpRegister = self.page.locator("#register > div > div > div.header > span")

    async def closePopUpHomePage(self):
        assert self.popUpHomePage, "Pop-up is not found"
        await self.popUpHomePage.click()

    async def pressBtnLogin(self):
        assert self.btnLogin, "Button Login is not found"
        await self.btnLogin.click()

    async def pressLinkRegister(self):
        assert self.linkRegister, "Link Register is not found"
        await self.linkRegister.click()
    
    async def pressBtnRegister(self):
        assert self.btnRegister, "Button Register is not found"
        await self.btnRegister.click()
        
    async def closePopUpRegister(self):
        time.sleep(1)
        assert self.popUpRegister, "Pop-up Register is not found"
        await self.popUpRegister.click()