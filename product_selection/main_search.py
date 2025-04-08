import sys
import os
import time
import asyncio
from playwright.async_api import async_playwright
from pages.search import HomeToSearchPage

URL = "https://automation-portal-bootcamp.vercel.app/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        homeToSearchPage = HomeToSearchPage(page)
        await homeToSearchPage.closePopUpHomePage()
        await homeToSearchPage.search_for_item("Paddle")
        time.sleep(3)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())