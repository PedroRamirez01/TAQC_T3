from playwright.async_api import Page
from config.config import Config

class ProductDetailPage:
    """
    Clase que representa la página de detalles del producto en el sitio web de prueba.
    Proporciona métodos para interactuar con los elementos de la página y realizar acciones como
    navegar a la página, agregar productos al carrito y verificar descuentos.
    Atributos:
        url (str): URL de la página de detalles del producto.
        page (Page): Instancia de la página de Playwright.
        title (Locator): Localizador para el título del producto.
        price (Locator): Localizador para el precio del producto.
        discount (Locator): Localizador para el descuento del producto.
        price_on_sale (Locator): Localizador para el precio en oferta del producto.
        span_color (Locator): Localizador para el color del producto.
        checked_input (Locator): Localizador para el input de color seleccionado.
        span_size (Locator): Localizador para el tamaño del producto.
        size_selected (Locator): Localizador para el tamaño seleccionado.
        input_quantity (Locator): Localizador para la cantidad del producto.
        add_to_cart (Locator): Localizador para el botón "Agregar al carrito".
        buy_with_btn (Locator): Localizador para el botón "Comprar con botón".
        cart_add_btn (Locator): Localizador para el botón "Agregar al carrito" en la vista emergente.
        cart_input (Locator): Localizador para la entrada de cantidad en la vista emergente del carrito.
        cart_close (Locator): Localizador para cerrar la vista emergente del carrito.
        shipping_text (Locator): Localizador para el texto de envío gratuito en la vista emergente del carrito.
    Métodos:
        navigate(): Navega a la página de detalles del producto.
        press_cart(): Presiona el botón "Agregar al carrito".
        cart_add_product(quantity: int): Agrega un producto al carrito con la cantidad especificada.
        verify_free_shipping(quantity: int): Verifica si el envío gratuito se aplica después de agregar productos al carrito.
        cart_add_cart(quantity: int): Verifica si la cantidad en el carrito se actualiza correctamente después de agregar productos.
        verify_discount(): Verifica si el descuento aplicado es correcto.
        add_to_cart_with_input(quantity: int): Agrega un producto al carrito utilizando un campo de entrada para la cantidad.
    """

    def __init__(self, page: Page) -> None:
        self.url = Config.URL_PRODUCT_DETAIL_PAGE
        self.page = page
        self.title = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-title")
        self.price = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-price > div.compare-at-price")
        self.discount = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-price > div.badges-on-sale > span")
        self.price_on_sale = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-price > div.price-on-sale")
        self.span_color = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker > div:nth-child(1) > div > span")
        self.checked_input = self.page.locator('input[type="radio"][name="color1"]:checked')
        self.span_size = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker > div:nth-child(2) > div > div")
        self.size_selected = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker > div:nth-child(2) > form")
        self.input_quantity = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > input[type=text]")
        self.add_to_cart = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > a.tf-btn.btn-fill.justify-content-center.fw-6.fs-16.flex-grow-1.animate-hover-btn")
        self.buy_with_btn = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > div > a.btns-full")
        self.cart_add_btn = self.page.locator("#shoppingCart > div > div > div.wrap > div.tf-mini-cart-wrap > div.tf-mini-cart-main > div > div.tf-mini-cart-items > div > div.tf-mini-cart-info > div.tf-mini-cart-btns > div.wg-quantity.small > span.btn-quantity.plus-btn")
        self.cart_input = self.page.locator("#shoppingCart > div > div > div.wrap > div.tf-mini-cart-wrap > div.tf-mini-cart-main > div > div.tf-mini-cart-items > div > div.tf-mini-cart-info > div.tf-mini-cart-btns > div.wg-quantity.small > input[type=text]")
        self.cart_close = self.page.locator("#shoppingCart > div > div > div.header > span")
        self.shipping_text = self.page.locator("#shoppingCart > div > div > div.wrap > div.tf-mini-cart-threshold > div.tf-progress-msg > span.price.fw-6")
        self.more_payment_option_link = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > div > a.payment-more-option")
        self.quantity_cart = self.page.locator("#shoppingCart > div > div > div.wrap > div.tf-mini-cart-wrap > div.tf-mini-cart-main > div > div.tf-mini-cart-items > div > div.tf-mini-cart-info > div.tf-mini-cart-btns > div.wg-quantity.small > input[type=text]")

    async def navigate(self) -> None:
        await self.page.goto(self.url, wait_until="domcontentloaded")

    async def press_cart(self) -> None:
        await self.add_to_cart.click()
        await self.page.wait_for_timeout(2000)

    async def cart_add_product(self, quantity: int) -> None:
        await self.press_cart()
        for _ in range(quantity):
            await self.cart_add_btn.click()

    async def verify_free_shipping(self, quantity: int) -> bool:
        await self.navigate()
        shipping_text_t1 = await self.shipping_text.inner_text()
        await self.cart_add_product(quantity)
        shipping_text_t2 = await self.shipping_text.inner_text()
        return shipping_text_t1 != shipping_text_t2

    async def cart_add_cart(self, quantity: int) -> bool:
        await self.navigate()
        await self.add_to_cart_with_input(quantity)
        input_t1 = await self.cart_input.input_value()
        await self.cart_close.click()
        await self.press_cart()
        input_t2 = await self.cart_input.input_value()
        return int(input_t1)*2 == int(input_t2)

    async def verify_discount(self) -> bool:
        await self.navigate()
        price = await self.price.inner_text()
        discount = await self.discount.inner_text()
        price_on_sale = await self.price_on_sale.inner_text()
        price = float(price.replace("$", "").replace(",", "").strip())
        price_on_sale = float(price_on_sale.replace("$", "").replace(",", "").strip())
        discount = float(discount)
        expected_price_on_sale = price - (price * discount / 100)
        return price_on_sale == expected_price_on_sale

    async def add_to_cart_with_input(self, quantity: int) -> bool:
        try:
            await self.navigate()
            if quantity == 0:
                quantity = 1
            await self.input_quantity.fill(str(quantity))
            await self.press_cart()
            input_value = await self.cart_input.input_value()
            return int(float(input_value)) == quantity
        except Exception as e:
            print(f"Error al añadir al carrito: {e}")
            return False
