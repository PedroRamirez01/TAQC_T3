import pytest
from playwright.async_api import Page
from utils.users_data import product_detail_quantity_input, product_detail_negative_quantity_input, product_detail_free_shipping, product_detail_cart_close_cart

"""_summary_
The following tests were performed using pytest and playwright:
    1. Discount verification: Verifies that the discount is applied correctly on
        the product details page.
    2. Regular amount in cart: Verifies that a regular amount can be added to the
        cart from the product details page.
    3. Negative or zero amount in cart: Verifies that a negative or zero amount 
        cannot be added to the cart from the product details page.
    4. Free shipping verification: Verifies that the 'Free Shipping' value changes
        when adding products to the cart from the product details page.
    5. Add and close cart: Verifies that a product can be added to the cart, closed,
        and then added the same amount to the cart again from the product details page.
"""

@pytest.mark.asyncio
async def test_verify_discount(product_detail_page: Page):
    assert await product_detail_page.verify_discount(), f"The discount is not correct. Price without discount: {await product_detail_page.price.inner_text()}, Discounted price: {await product_detail_page.price_on_sale.inner_text()}, Discount: {await product_detail_page.discount.inner_text()}%."

@pytest.mark.asyncio
@pytest.mark.parametrize("quantity", product_detail_quantity_input)
async def test_product_detail_quantity_with_input_normal_quantity(product_detail_page: Page, quantity: int):
    assert await product_detail_page.add_to_cart_with_input(quantity), f"The quantity could not be added correctly: {quantity}."
    cantidad = int(float(await product_detail_page.quantity_cart.input_value()))
    assert 0 < cantidad < 10000, f"Quantity in cart out of range."
    assert cantidad == quantity, f"Quantity in cart does not match the quantity added: {cantidad} != {quantity}."

@pytest.mark.asyncio
@pytest.mark.parametrize("quantity", product_detail_negative_quantity_input)
async def test_product_detail_negative_quantity_with_input_normal_quantity(product_detail_page: Page, quantity: int):
    assert not await product_detail_page.add_to_cart_with_input(quantity), f"A negative amount or 0 was accepted."
    cantidad = int(float(await product_detail_page.quantity_cart.input_value()))
    assert cantidad == 1, f"Negative values ​​can be entered in quantity input."

@pytest.mark.asyncio
@pytest.mark.parametrize("quantity", product_detail_free_shipping)
async def test_verify_free_shipping(product_detail_page: Page, quantity: int):
    assert await product_detail_page.verify_free_shipping(quantity), "The value shown in 'Free Shipping' does not change after adding more products."

@pytest.mark.asyncio
@pytest.mark.parametrize("quantity", product_detail_cart_close_cart)
async def test_product_detail_add_to_cart_close_add_to_cart(product_detail_page: Page, quantity: int):
    assert await product_detail_page.cart_add_cart(quantity), f"It is added {quantity+1} products, add to cart is pressed, cart is closed, the same value is added to the cart again, but the value does not change in the cart."

