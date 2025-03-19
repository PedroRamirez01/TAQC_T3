import asyncio
import time
from playwright.async_api import async_playwright

# from pages.login import Login
from pages.register import RegisterPage

URL = "https://automation-portal-bootcamp.vercel.app/register"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")

        # await page.locator("#newsletterPopup > div > div > div.modal-top > span").click()
        # await page.locator("#header > div > div > div.col-xxl-5.col-md-4.col-3 > ul > li.nav-account > a").click()
        # await page.locator("#login > div > div > div.tf-login-form > form > div.bottom > div:nth-child(2) > a").click()
        # await page.locator("#register > div > div > div.tf-login-form > form > div.bottom > div:nth-child(1) > a").click()

        registerPage = RegisterPage(page)
        await registerPage.register("John", "Doe", "Jhon123@gmail.com", "Password123")

        time.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())