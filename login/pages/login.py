from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHomePage = self.page.locator("#newsletterPopup > div > div > div.modal-top > span")
        self.btnProfile = self.page.locator("#header > div > div > div.col-xxl-5.col-md-4.col-3 > ul > li.nav-account > a")
        self.fieldEmail = self.page.locator("#loginEmail")
        self.fieldPassword = self.page.locator("#loginPassword")
        self.btnLogin = self.page.locator("#login > div > form > div:nth-child(4) > button")

    async def closePopUpHomePage(self):
        await self.popUpHomePage.wait_for()
        assert self.popUpHomePage, "Pop-up is not found"
        await self.popUpHomePage.click()

    async def pressBtnProfile(self):
        await self.btnProfile.wait_for()
        assert self.btnProfile, "Button Login is not found"
        await self.btnProfile.click()

    async def loginEmail(self, email: str):
        assert email, "Email is empty"
        await self.page.fill("#loginEmail", email)

    async def loginPassword(self, password: str):
        assert password, "Password is empty"
        await self.page.fill("#loginPassword", password)

    async def pressBtnLogin(self):
        assert await self.btnLogin, "Button Login is not found"
        await self.btnLogin.click()

# from playwright.async_api import Page

# class LoginPage:
#     def __init__(self, page: Page):
#         self.page = page
#         self.btnProfile = self.page.locator("#header > div > div > div.col-xxl-5.col-md-4.col-3 > ul > li.nav-account > a")
#         self.fieldEmail = self.page.locator("#loginEmail")
#         self.fieldPassword = self.page.locator("#loginPassword")
#         self.btnLogin = self.page.locator("#login > div > form > div:nth-child(4) > button")

#     async def closePopUpHomePage(self):
#         await self.page.wait_for_selector("#newsletterPopup > div > div > div.modal-top > span")
#         await self.page.locator("#newsletterPopup > div > div > div.modal-top > span").click()

#     async def pressBtnProfile(self):
#         assert await self.btnProfile, "Button Login is not found"
#         await self.btnProfile.click()

#     async def loginEmail(self, email: str):
#         assert email, "Email is empty"
#         await self.page.fill("#loginEmail", email)

#     async def loginPassword(self, password: str):
#         assert password, "Password is empty"
#         await self.page.fill("#loginPassword", password)

#     async def pressBtnLogin(self):
#         assert await self.btnLogin, "Button Login is not found"
#         await self.btnLogin.click()
