import pytest
from pages.addToCart_page import AddToCart
from utils.test_data import valid_checkout_data, invalid_checkout_data
from playwright.async_api import expect

test_data = valid_checkout_data + invalid_checkout_data

@pytest.mark.asyncio 
@pytest.mark.parametrize("label,data", test_data)
async def test_checkout_flow(label, data,checkout_page, add_to_cart):
       
        await add_to_cart.closeModal()
        await add_to_cart.clickFirstPaddle()
        await add_to_cart.performAddToCartActions()

        await checkout_page.clickTermsAndConditionsCheckbox()
        await checkout_page.clickProceedToCheckoutButton()

        await checkout_page.fillCheckoutForm(data)
        await checkout_page.clickAgreeCheckbox()
        await checkout_page.clickPlaceOrderButton()

        await checkout_page.page.wait_for_timeout(5000) 

        await expect(checkout_page.successMessage).to_contain_text("Order saved successfully! Your order ID is:")

        order_id = await checkout_page.getOrderId()
        print(f"Order ID: {order_id}")

        order = await checkout_page.getOrderbyId(order_id)
        print(f"Order: {order}")

        assert order["items"][0]["title"] == 'Franklin Signature Pickleball Paddle'
        assert order["items"][0]["quantity"] == 5
        assert order["items"][0]["price"] == 100

@pytest.mark.asyncio
@pytest.mark.parametrize("label,data", valid_checkout_data)
async def test_checkout_with_empty_cart(label, data,checkout_page, add_to_cart):

        await add_to_cart.closeModal()
        await add_to_cart.clickCartButton()

        await checkout_page.page.wait_for_timeout(2000)
        await checkout_page.clickTermsAndConditionsCheckbox()
        await checkout_page.clickProceedToCheckoutButton()
        await checkout_page.fillCheckoutForm(data)
        await checkout_page.clickAgreeCheckbox()
        await checkout_page.clickPlaceOrderButton()

        await checkout_page.page.wait_for_timeout(5000)

        await expect(checkout_page.successMessage).to_contain_text("Order saved successfully! Your order ID is:")

        order_id = await checkout_page.getOrderId()
        print(f"Order ID: {order_id}")

        order = await checkout_page.getOrderbyId(order_id)
        print(f"Order: {order}")


