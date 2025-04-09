import asyncio
from playwright.async_api import async_playwright
import time
from pages_checkout.homeToProductD import HomeToProductDetails
from pages_checkout.addToCart import AddToCart
from pages_checkout.checkoutPage import CheckoutPage

URL = "https://automation-portal-bootcamp.vercel.app/"

happy_path = [ # no pasa porque el discount code está vacío
    {
        "FIRST_NAME": "Pedrito",
        "LAST_NAME": "González",
        "COUNTRY": "United States", 
        "CITY": "Springfield",
        "ADRESS": "Calle siempre viva 123",
        "PHONE_NUMBER": "123456789",
        "EMAIL": "pedritogonzalez123@gmail.com",
        "DISCOUNT_CODE": "",
        "CARD_NUMBER": "4242424242424242",
        "CARD_EXPIRATION": "12/25",
        "CARD_CVV": "123"
    }
]

sad_path = [
    {
        "FIRST_NAME": "#",
        "LAST_NAME": "$",
        "COUNTRY": "United States", 
        "CITY": "?",
        "ADRESS": "#",
        "PHONE_NUMBER": "&",
        "EMAIL": "pedritogonzalez123@gmail.com",
        "DISCOUNT_CODE": "123456",
        "CARD_NUMBER": "4242424242424242",
        "CARD_EXPIRATION": "12/25",
        "CARD_CVV": "123"
    }
]

path = sad_path

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
        await checkoutpage.fillFirstName(path[0]["FIRST_NAME"])
        await checkoutpage.fillLastName(path[0]["LAST_NAME"])
        await checkoutpage.fillCountry(path[0]["COUNTRY"])
        await checkoutpage.fillCity(path[0]["CITY"])
        await checkoutpage.fillAdress(path[0]["ADRESS"])
        await checkoutpage.fillPhoneNumber(path[0]["PHONE_NUMBER"])
        await checkoutpage.fillEmail(path[0]["EMAIL"])  
        await checkoutpage.fillDiscountCode(path[0]["DISCOUNT_CODE"])
        await checkoutpage.fillCardNumber(path[0]["CARD_NUMBER"])
        await checkoutpage.fillCardExpiration(path[0]["CARD_EXPIRATION"])
        await checkoutpage.fillCardCVV(path[0]["CARD_CVV"])
        await checkoutpage.clickAgreeCheckbox()
        await checkoutpage.clickPlaceOrderButton()

        time.sleep(10)

        await browser.close()



if __name__ == "__main__":
    asyncio.run(main())
