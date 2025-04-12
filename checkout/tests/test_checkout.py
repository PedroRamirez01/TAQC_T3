import pytest
import asyncio
from playwright.async_api import async_playwright
import time
from pages_checkout.homeToProductD import HomeToProductDetails
from pages_checkout.addToCart import AddToCart
from pages_checkout.checkoutPage import CheckoutPage

URL = "https://automation-portal-bootcamp.vercel.app/"

test_data = [
    ("valid_data", { # no pasa porque el discount code está vacío
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
    }),
    ("invalid_data",{
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
    }),
    ("no_data", {
        "FIRST_NAME": "",
        "LAST_NAME": "",
        "COUNTRY": "", 
        "CITY": "",
        "ADRESS": "",
        "PHONE_NUMBER": "",
        "EMAIL": "",
        "DISCOUNT_CODE": "",
        "CARD_NUMBER": "",
        "CARD_EXPIRATION": "",
        "CARD_CVV": ""
    }),
]

@pytest.mark.asyncio
@pytest.mark.parametrize("label,data", test_data)
async def test_checkout_flow(label,data,page):
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
        await addToCart.incrementQuantity()
        await addToCart.incrementQuantity()
        await addToCart.decrementQuantity()
        await addToCart.addToCart()

        checkoutpage = CheckoutPage(page)
        await checkoutpage.clickTermsAndConditionsCheckbox()
        await checkoutpage.clickProceedToCheckoutButton()
        await checkoutpage.fillFirstName(data["FIRST_NAME"])
        await checkoutpage.fillLastName(data["LAST_NAME"])
        await checkoutpage.fillCountry(data["COUNTRY"])
        await checkoutpage.fillCity(data["CITY"])
        await checkoutpage.fillAdress(data["ADRESS"])
        await checkoutpage.fillPhoneNumber(data["PHONE_NUMBER"])
        await checkoutpage.fillEmail(data["EMAIL"])  
        await checkoutpage.fillDiscountCode(data["DISCOUNT_CODE"])
        await checkoutpage.fillCardNumber(data["CARD_NUMBER"])
        await checkoutpage.fillCardExpiration(data["CARD_EXPIRATION"])
        await checkoutpage.fillCardCVV(data["CARD_CVV"])
        await checkoutpage.clickAgreeCheckbox()
        await checkoutpage.clickPlaceOrderButton()

        success_message = page.locator("text=Order saved successfully!")

        if label == "valid_data":
            assert await success_message.is_visible(), "Expected success message not found."
        else:
            assert not await success_message.is_visible(), "Unexpected success message found for invalid input."

        time.sleep(5)