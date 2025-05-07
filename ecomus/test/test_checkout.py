import pytest
from pages.addToCart import AddToCart
from pages.checkoutPage import CheckoutPage
from utils.test_data import valid_checkout_data, invalid_checkout_data

product_id = 1
URL = f"https://automation-portal-bootcamp.vercel.app/product-detail/{product_id}"

test_data = valid_checkout_data + invalid_checkout_data

@pytest.mark.asyncio
@pytest.mark.parametrize("label,data", test_data)
async def test_checkout_flow(label,data,page):
        await page.goto(URL, wait_until="domcontentloaded")
        addToCart = AddToCart(page)
        await addToCart.perform_add_to_cart_actions()

        checkoutpage = CheckoutPage(page)
        await checkoutpage.clickTermsAndConditionsCheckbox()
        await checkoutpage.clickProceedToCheckoutButton()

        await checkoutpage.fill_checkout_form(data)
        await checkoutpage.clickAgreeCheckbox()
        await checkoutpage.clickPlaceOrderButton()

        await page.wait_for_timeout(5000) 

        await checkoutpage.assert_success_message(label)

@pytest.mark.asyncio
@pytest.mark.parametrize("label,data", valid_checkout_data)
async def test_checkout_with_empty_cart(label,data,page):
        await page.goto(URL, wait_until="domcontentloaded")

        cart_button = page.locator("#header > div > div > div.col-xl-3.col-md-4.col-3 > ul > li.nav-cart > a")
        await cart_button.click()
        await page.wait_for_timeout(2000)

        checkoutpage = CheckoutPage(page)
        await checkoutpage.clickTermsAndConditionsCheckbox()
        await checkoutpage.clickProceedToCheckoutButton()
        await checkoutpage.fill_checkout_form(data)
        await checkoutpage.clickAgreeCheckbox()
        await checkoutpage.clickPlaceOrderButton()

        await page.wait_for_timeout(5000) 

        await checkoutpage.assert_success_message(label)
