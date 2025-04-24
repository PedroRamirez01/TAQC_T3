# import pytest
# from playwright.async_api import Page
# from utils.users_data import product_detail_quantity_input, product_detail_negative_quantity_input, product_detail_free_shipping, product_detail_cart_close_cart

# @pytest.mark.asyncio
# async def test_verify_discount(product_detail_page: Page):
#     """
#     Verifica que el descuento se aplique correctamente en la página de detalles del producto.
#     """
#     assert await product_detail_page.verify_discount(), f"El descuento no es correcto. Precio sin descuento: {await product_detail_page.price.inner_text()}, Precio con descuento: {await product_detail_page.price_on_sale.inner_text()}, Descuento: {await product_detail_page.discount.inner_text()}%."

# @pytest.mark.asyncio
# @pytest.mark.parametrize("quantity", product_detail_quantity_input)
# async def test_product_detail_quantity_with_input_normal_quantity(product_detail_page: Page, quantity: int):
#     """
#     Verifica que se pueda añadir una cantidad normal al carrito desde la página de detalles del producto.
#     """
#     assert await product_detail_page.add_to_cart_with_input(quantity), f"No se pudo añadir correctamente la cantidad: {quantity}"
#     cantidad = int(float(await product_detail_page.quantity_cart.input_value()))
#     assert 0 < cantidad < 10000, f"Cantidad en el carrito fuera de rango."
#     assert cantidad == quantity, f"Cantidad en el carrito no coincide con la cantidad añadida: {cantidad} != {quantity}"

# @pytest.mark.asyncio
# @pytest.mark.parametrize("quantity", product_detail_negative_quantity_input)
# async def test_product_detail_negative_quantity_with_input_normal_quantity(product_detail_page: Page, quantity: int):
#     """
#     Verifica que no se pueda añadir una cantidad negativa o cero al carrito desde la página de detalles del producto.
#     """
#     assert not await product_detail_page.add_to_cart_with_input(quantity), f"Se aceptó una cantidad negativa o 0."
#     cantidad = int(float(await product_detail_page.quantity_cart.input_value()))
#     assert cantidad == 1, f"Se puede ingresar valores negativos en input de cantidad."

# @pytest.mark.asyncio
# @pytest.mark.parametrize("quantity", product_detail_free_shipping)
# async def test_verify_free_shipping(product_detail_page: Page, quantity: int):
#     """
#     Verifica que el valor de 'Free Shipping' cambie al añadir productos al carrito desde la página de detalles del producto.
#     """
#     assert await product_detail_page.verify_free_shipping(quantity), "El valor que se muestra en el 'Free Shipping' no cambia despues de añadir más productos."

# @pytest.mark.asyncio
# @pytest.mark.parametrize("quantity", product_detail_cart_close_cart)
# async def test_product_detail_add_to_cart_close_add_to_cart(product_detail_page: Page, quantity: int):
#     """
#     Verifica que se pueda añadir un producto al carrito, cerrar el carrito y luego añadir nuevamente el mismo valor al carrito desde la página de detalles del producto.
#     """
#     assert await product_detail_page.cart_add_cart(quantity), f"Se añade {quantity+1} productos, se presiona añadir al carrito, se cierra carrito, se añade nuevamente el mismo valor al carrito, pero el valor no cambia en el carrito."

