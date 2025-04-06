import asyncio
from playwright.async_api import async_playwright
import time
from pages_checkout.homeToProductD import HomeToProductDetails
from pages_checkout.addToCart import AddToCart
from pages_checkout.checkoutPage import CheckoutPage

URL = "https://automation-portal-bootcamp.vercel.app/"

async def main():
    async with async_playwright() as p:   
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL, wait_until="domcontentloaded")


        homeToProductDetails = HomeToProductDetails(page)
        await homeToProductDetails.closePopup()
        await homeToProductDetails.clickFirstCollection()
        await homeToProductDetails.clickFirstProduct()

        addToCart = AddToCart(page)
        await addToCart.changeColor()
        await addToCart.changeSize()
        await addToCart.incrementQuantity()
        await addToCart.incrementQuantity()
        await addToCart.incrementQuantity()
        await addToCart.decrementQuantity()
        await addToCart.addToCart()

        checkoutpage = CheckoutPage(page)
        await checkoutpage.clickTermsAndConditionsCheckbox()
        await checkoutpage.clickProceedToCheckoutButton()

        time.sleep(10)

        await browser.close()



if __name__ == "__main__":
    asyncio.run(main())
