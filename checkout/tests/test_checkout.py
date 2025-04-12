import pytest
import asyncio
from playwright.async_api import async_playwright
import time
from pages_checkout.homeToProductD import HomeToProductDetails
from pages_checkout.addToCart import AddToCart
from pages_checkout.checkoutPage import CheckoutPage
from utils.test_data import test_data_checkout

URL = "https://automation-portal-bootcamp.vercel.app/"

@pytest.mark.asyncio
@pytest.mark.parametrize("label,data", test_data_checkout)
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