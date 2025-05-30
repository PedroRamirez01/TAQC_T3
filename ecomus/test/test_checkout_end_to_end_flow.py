import pytest
from playwright.async_api import Page
from playwright.async_api import expect

@pytest.mark.asyncio
@pytest.mark.parametrize("auto_delete_user_e2e", [{
    "email": "luis.rodriguez@gmail.com"
}], indirect=True)
async def test_checkoutbug(register_page: Page, login_page: Page, homeTo_page: Page, add_to_cart: Page, checkout_page:Page, auto_delete_user_e2e): #, home_page: Page, add_to_cart: Page, checkout_page: Page
    await register_page.navigate()
    await register_page.fill_register_form({
        "first_name": "Luis",
        "last_name": "Rodriguez",
        "email": "luis.rodriguez@gmail.com",
        "password": "Rl1254sZ",
    })
    await register_page.submit()
    
    await expect(register_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/login")
    await login_page.fill_login_form({
        "email": "luis.rodriguez@gmail.com",
        "password": "Rl1254sZ",
    })
    await expect(login_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/my-account")

    await homeTo_page.click_ecomus()
    await homeTo_page.close_pop_up_home()
    await add_to_cart.clickFirstPaddle()
    await add_to_cart.changeColor("Beige")
    await add_to_cart.changeSize("M")
    await add_to_cart.incrementQuantity()
    await add_to_cart.decrementQuantity()
    await add_to_cart.setItemQuantity(2)
    await add_to_cart.addToCart()
    await checkout_page.clickTermsAndConditionsCheckbox()
    await checkout_page.clickProceedToCheckoutButton()

    await checkout_page.fillCheckoutForm({
        "FIRST_NAME": "",
        "LAST_NAME": "Rodriguez",
        "COUNTRY": "United States",
        "CITY": "Springfield",
        "ADDRESS": "Calle siempre viva 123",
        "PHONE_NUMBER": "123456789",
        "EMAIL": "luis.rodriguez@gmail.com",
        "DISCOUNT_CODE": "123",
        "CARD_NUMBER": "4242424242424242",
        "CARD_EXPIRATION": "12/25",
        "CARD_CVV": "123"
    })
    await checkout_page.clickAgreeCheckbox()
    await checkout_page.clickPlaceOrderButton()
    await expect(checkout_page.successMessage).not_to_be_visible()

    order_id = await checkout_page.getOrderId()
    print(f"Order ID: {order_id}")

    order = await checkout_page.getOrderbyId(order_id)
    print(f"Order: {order}")

    assert order["items"][0]["title"] == 'Franklin Signature Pickleball Paddle'
    assert order["items"][0]["quantity"] == 2
    assert order["items"][0]["price"] == 100