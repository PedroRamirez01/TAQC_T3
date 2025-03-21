import asyncio
import time
from playwright.async_api import async_playwright

from pages.login import LoginPage
from pages.register import RegisterPage
from pages.homeToRegister import HomeToRegisterPage

URL = "https://automation-portal-bootcamp.vercel.app/"

happy_path = [
    {
        "FIRST_NAME": "José",
        "LAST_NAME": "Hernández",
        "EMAIL": "jh_happy_path@gmail.com",
        "PASSWORD": "2&3df5g"
    }
]

sad_path = [
    {
        "FIRST_NAME": "#",
        "LAST_NAME": "$",
        "EMAIL": "jh_sad_path@gmail.com",
        "PASSWORD": "2&3df5g"
    }
]

path = sad_path

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
        await registerPage.registerFirstName(path[0]["FIRST_NAME"])
        await registerPage.registerLastName(path[0]["LAST_NAME"])
        await registerPage.registerEmail(path[0]["EMAIL"])
        await registerPage.registerPassword(path[0]["PASSWORD"])
        await registerPage.pressBtnRegister()

        time.sleep(5)

        loginPage = LoginPage(page)
        await loginPage.loginEmail(path[0]["EMAIL"])
        await loginPage.loginPassword(path[0]["PASSWORD"])
        await loginPage.pressBtnLogin()

        time.sleep(5)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())