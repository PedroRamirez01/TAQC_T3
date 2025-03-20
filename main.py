import asyncio
import time
from playwright.async_api import async_playwright

from pages.login import LoginPage
from pages.register import RegisterPage
from pages.homeToRegister import HomeToRegisterPage

URL = "https://automation-portal-bootcamp.vercel.app/"

FIRST_NAME = "José"
LAST_NAME = "Hernández"
EMAIL = "jh@gmail.com"
PASSWORD = "jh12345"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")

        homeToRegisterPage = HomeToRegisterPage(page)
        await homeToRegisterPage.closePopUpHomePage()
        await homeToRegisterPage.pressBtnLogin()
        await homeToRegisterPage.pressLinkRegister()
        await homeToRegisterPage.pressBtnRegister()
        await homeToRegisterPage.closePopUpRegister()

        time.sleep(2)

        registerPage = RegisterPage(page)
        await registerPage.registerFirstName(FIRST_NAME)
        await registerPage.registerLastName(LAST_NAME)
        await registerPage.registerEmail(EMAIL)
        await registerPage.registerPassword(PASSWORD)
        await registerPage.pressBtnRegister()

        time.sleep(2)

        loginPage = LoginPage(page)
        await loginPage.loginEmail(EMAIL)
        await loginPage.loginPassword(PASSWORD)
        await loginPage.pressBtnLogin()

        time.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())