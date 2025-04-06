import sys
import os
import time
import asyncio
from playwright.async_api import async_playwright
from pages_product_selection.search import HomeToSearchPage
from pages_product_selection.filter_product import FilterProductPage


URL = "https://automation-portal-bootcamp.vercel.app/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        closePopUp = HomeToSearchPage(page)
        await closePopUp.closePopUpHomePage()

        searchProduct = FilterProductPage(page)
        await searchProduct.searchIcon.click()
        await searchProduct.qckLink()
        await searchProduct.doFilter()
        await searchProduct.PopUp()
        time.sleep(3)


        
        await browser.close()

if __name__ == "__main_2__":
    asyncio.run(main())