import asyncio
from config.config import Config
from playwright.async_api import async_playwright
from pages.search_page import HomeToSearchPage

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(Config.URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        homeToSearchPage = HomeToSearchPage(page)
        await homeToSearchPage.closePopUpHomePage()
        await homeToSearchPage.searchIcons()
        await homeToSearchPage.search_for_item("Paddle", max_attempts=2, delay=2000)
        await page.wait_for_timeout(2000)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())