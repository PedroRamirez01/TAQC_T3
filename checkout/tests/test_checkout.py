import pytest
import asyncio
from playwright.async_api import async_playwright
from playwright.async_api import Page
import time
from pages_checkout.homeToProductD import HomeToProductDetails
from pages_checkout.addToCart import AddToCart
from pages_checkout.checkoutPage import CheckoutPage
from utils.test_data import valid_checkout_data, invalid_checkout_data

URL = "https://automation-portal-bootcamp.vercel.app/product-detail/1"

test_data = valid_checkout_data + invalid_checkout_data

@pytest.mark.asyncio
@pytest.mark.parametrize("label,data", test_data)
async def test_checkout_flow(label,data,page):
        await page.goto(URL, wait_until="domcontentloaded")

        # homeToProductDetails = HomeToProductDetails(page)
        # await homeToProductDetails.closePopup()
        # await homeToProductDetails.clickFirstCollection()
        # await homeToProductDetails.clickFirstProduct()

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
        await checkoutpage.fillAdress(data["ADDRESS"])
        await checkoutpage.fillPhoneNumber(data["PHONE_NUMBER"])
        await checkoutpage.fillEmail(data["EMAIL"])  
        await checkoutpage.fillDiscountCode(data["DISCOUNT_CODE"])
        await checkoutpage.fillCardNumber(data["CARD_NUMBER"])
        await checkoutpage.fillCardExpiration(data["CARD_EXPIRATION"])
        await checkoutpage.fillCardCVV(data["CARD_CVV"])
        await checkoutpage.clickAgreeCheckbox()
        await checkoutpage.clickPlaceOrderButton()

        await page.wait_for_timeout(5000) 

        # Los label con missing pasan, ya que no se hace la compra, pero deberian mostrar un mensaje de "invalid input ??"

        success_message = page.locator("#wrapper > section > div > div > div.tf-page-cart-footer > div > form > p:nth-child(9)")

        if label.startswith("valid"):
            assert await success_message.is_visible(), f"[{label}] Expected success message not found."
        else:
            assert not await success_message.is_visible(), f"[{label}] Unexpected success message for invalid input."

