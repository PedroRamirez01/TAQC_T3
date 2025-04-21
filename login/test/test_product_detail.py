import pytest
from playwright.async_api import Page
from utils.users_data import product_detail_quantity_btn, product_detail_quantity_input

#*
# Test a realizar
# Probar boton cambio de producto
# Compara span de precio y rebaja, y ver si corresponde al porcentaje puesto
# Seleccionar producto(Para todos los test, seleccionar varios productos y dar info del producto en caso de error) 
# Probar cambio de color y verificar span de color
# Cambiar tamaño y verificar span de tamaño
# Ingresar valores a input de Quality con diferentes productos, y diferentes cantidades
# Añadir al carro, validar que numero de productos ingresados, correspondan a los que se encuentran en el carro
# Añadir a favoritos
# Comparacion de diferentes productos
# Probar funcionalidad buy with ******
# boton more payments option
# Compare color
# ask questions
# Delivery and Return
# Share option
# *#

@pytest.mark.asyncio
async def test_verify_discount(product_detail_page: Page):
    assert await product_detail_page.verify_discount(), f"El descuento no es correcto. Precio sin descuento: {await product_detail_page.price.inner_text()}, Precio con descuento: {await product_detail_page.price_on_sale.inner_text()}, Descuento: {await product_detail_page.discount.inner_text()}%."

@pytest.mark.asyncio
@pytest.mark.parametrize("quantity", product_detail_quantity_btn)
async def test_product_detail_quantity_with_btn_add_normal_quantity(product_detail_page: Page, quantity):
    await product_detail_page.add_to_cart_with_btn_add(quantity)
    assert await product_detail_page.quantity_cart.input_value() == str(quantity+1), f"Cantidad en el carrito no coincide con la cantidad añadida: {await product_detail_page.quantity_cart.input_value()} != {quantity+1}"

@pytest.mark.asyncio
@pytest.mark.parametrize("quantity", product_detail_quantity_input)
async def test_product_detail_quantity_with_input_normal_quantity(product_detail_page: Page, quantity):
    await product_detail_page.add_to_cart_with_input(quantity)
    assert await product_detail_page.quantity_cart.input_value() == str(quantity), f"Cantidad en el carrito no coincide con la cantidad añadida: {await product_detail_page.quantity_cart.input_value()} != {quantity+1}"
