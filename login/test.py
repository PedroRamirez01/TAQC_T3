import asyncio
import time
from playwright.async_api import async_playwright

from pages.login import LoginPage

URL = "https://automation-portal-bootcamp.vercel.app/"

happy_path = [
    {
        "EMAIL": "pedro@gmail.com",
        "PASSWORD": "123456"
    }
]

sad_path = [
    {
        "EMAIL": "pedro@gmail.com",
        "PASSWORD": "123456"
    }
]

path = happy_path

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")

        loginPage = LoginPage(page)
        await loginPage.closePopUpHomePage()
        # await loginPage.pressBtnProfile()
        # await loginPage.loginEmail(path[0]["EMAIL"])
        # await loginPage.loginPassword(path[0]["PASSWORD"])
        # await loginPage.pressBtnLogin()

        time.sleep(5)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())