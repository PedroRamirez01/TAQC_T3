import asyncio
from playwright.async_api import async_playwright

from pages.register import RegisterPage
from pages.homeToRegister import HomeToRegisterPage

URL = "https://automation-portal-bootcamp.vercel.app/"

happy_path = [
    {
        "FIRST_NAME": "José11",
        "LAST_NAME": "Hernández11",
        "EMAIL": "jh_happy_path11@gmail.com",
        "PASSWORD": "2&3df5g11"
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

path = happy_path

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

        registerPage = RegisterPage(page)
        await registerPage.registerFirstName(path[0]["FIRST_NAME"])
        await registerPage.registerLastName(path[0]["LAST_NAME"])
        await registerPage.registerEmail(path[0]["EMAIL"])
        await registerPage.registerPassword(path[0]["PASSWORD"])
        await registerPage.pressBtnRegister()

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())