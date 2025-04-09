import sys
import os
import asyncio
from playwright.async_api import async_playwright
from pages.search import HomeToSearchPage
from pages.filter_product import FilterProductPage


URL = "https://automation-portal-bootcamp.vercel.app/"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(3000)

        closePopUp = HomeToSearchPage(page)
        closePopUp.closePopUpHomePage()

        searchProduct = FilterProductPage(page)
        await searchProduct.searchIcon.click()
        await searchProduct.qckLink()
        await searchProduct.doFilterMen()
        await searchProduct.PopUp()
        await searchProduct.takeScreenshot(path="same_product1.png", fullPage=True)
        await searchProduct.doFilterWomen()
        await searchProduct.PopUp()
        await searchProduct.takeScreenshot(path="same_product2.png", fullPage=True)
        # Comparar divs, pytest
        
        await browser.close()

if __name__ == "__main_2__":
    asyncio.run(main())