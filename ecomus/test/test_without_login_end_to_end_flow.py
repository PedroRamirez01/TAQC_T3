import pytest
from playwright.async_api import Page
from playwright.async_api import expect

@pytest.mark.asyncio
@pytest.mark.parametrize("auto_delete_user_e2e", [{
    "email": "luis.rodriguez@gmail.com"
}], indirect=True)
async def test_successful(homeTo_page: Page, add_to_cart: Page, checkout_page: Page, auto_delete_user_e2e):
    await homeTo_page.navigate()

    await expect(homeTo_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/")

    await homeTo_page.close_pop_up_home()
    await add_to_cart.clickThirdPaddle()
    await add_to_cart.changeColor("Black")
    await add_to_cart.changeSize("M")
    await add_to_cart.incrementQuantity()
    await add_to_cart.addToCart()

    await checkout_page.clickTermsAndConditionsCheckbox()
    await checkout_page.clickProceedToCheckoutButton()

    await checkout_page.fillCheckoutForm({
        "FIRST_NAME": "Luis",
        "LAST_NAME": "Rodriguez",
        "COUNTRY": "United States",
        "CITY": "Springfield",
        "ADDRESS": "Av. Siempreviva 742",
        "PHONE_NUMBER": "987654321",
        "EMAIL": "luis.rodriguez@gmail.com",
        "DISCOUNT_CODE": "123456",
        "CARD_NUMBER": "4242424242424242",
        "CARD_EXPIRATION": "12/25",
        "CARD_CVV": "000"
    })
    await checkout_page.clickAgreeCheckbox()
    await checkout_page.clickPlaceOrderButton()
    await expect(checkout_page.successMessage).to_contain_text("Order saved successfully! Your order ID is:")

    order_id = await checkout_page.getOrderId()

    order = await checkout_page.getOrderbyId(order_id)

    assert order["items"][0]["title"] == 'JOOLA Scorpeus Pickleball Paddle', f"Expected title 'JOOLA Scorpeus Pickleball Paddle', got {order['items'][0]['title']}"
    assert order["items"][0]["quantity"] == 2, f'Expected quantity 2, got {order["items"][0]["quantity"]}. Product: {order["items"][0]["title"]}'
    assert order["items"][0]["price"] == 199, f'Expected price 100, got {order["items"][0]["price"]}. Product: {order["items"][0]["title"]}'