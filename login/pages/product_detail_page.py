from playwright.async_api import Page
from config.config import Config

class ProductDetailPage:
    """_summary_
    Clase que representa la página de detalles del producto en el sitio web de prueba.
    Proporciona métodos para interactuar con los elementos de la página y obtener información sobre el producto.

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
        size_selected (Locator): Localizador para el tamaño seleccionado del producto.
        less_quantity (Locator): Localizador para el botón de disminuir cantidad.
        input_quantity (Locator): Localizador para el input de cantidad.
        add_quantity (Locator): Localizador para el botón de aumentar cantidad.
        add_to_cart (Locator): Localizador para el botón "Añadir al carrito".
        buy_with_btn (Locator): Localizador para el botón "Comprar con...".
        more_payment_option_link (Locator): Localizador para el enlace "Más opciones de pago".
        quantity_cart (Locator): Localizador para la cantidad en el carrito.
    Métodos:
        navigate(): Navega a la página de detalles del producto.
        get_info(): Obtiene información del producto (título, precio, descuento y precio en oferta).
        verify_discount(): Verifica si el descuento aplicado es correcto.
        verify_color(): Verifica si el color seleccionado es correcto.
        add_to_cart_with_btn_add(quantity): Añade el producto al carrito utilizando el botón de aumentar cantidad.
        add_to_cart_with_input(quantity): Añade el producto al carrito utilizando el input de cantidad.
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
        self.less_quantity = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.minus-btn")
        self.input_quantity = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > input[type=text]")
        self.add_quantity = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.plus-btn")
        self.add_to_cart = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > a.tf-btn.btn-fill.justify-content-center.fw-6.fs-16.flex-grow-1.animate-hover-btn")
        self.buy_with_btn = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > div > a.btns-full")
        self.more_payment_option_link = self.page.locator("#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > div > a.payment-more-option")
        self.quantity_cart = self.page.locator("#shoppingCart > div > div > div.wrap > div.tf-mini-cart-wrap > div.tf-mini-cart-main > div > div.tf-mini-cart-items > div > div.tf-mini-cart-info > div.tf-mini-cart-btns > div.wg-quantity.small > input[type=text]")

    async def navigate(self) -> None:
        await self.page.goto(self.url, wait_until="domcontentloaded")

    async def get_info(self) -> dict:
        await self.navigate()
        title = await self.title.inner_text()
        price = await self.price.inner_text()
        discount = await self.discount.inner_text()
        price_on_sale = await self.price_on_sale.inner_text()
        return {
            "title": title,
            "price": price,
            "discount": discount,
            "price_on_sale": price_on_sale
        }

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

    async def verify_color(self) -> bool:
        await self.navigate()
        checked_input = self.page.locator('input[type="radio"][name="color1"]:checked').first
        color_selected = await checked_input.inner_text()
        span_color_text = await self.span_color.inner_text()
        print(f"Color seleccionado: {color_selected}")
        print(f"Color esperado: {span_color_text}")
        return color_selected.strip().lower() == span_color_text.strip().lower()

    async def add_to_cart_with_btn_add(self, quantity) -> None:
        try:    
            await self.navigate()
            for _ in range(quantity):
                await self.add_quantity.click()
            await self.add_to_cart.click()
            await self.page.wait_for_timeout(2000)
        except Exception as e:
            assert f"Error al añadir al carrito: {e}"

    async def add_to_cart_with_input(self, quantity) -> None:
        try:
            await self.navigate()
            await self.input_quantity.fill(str(quantity))
            await self.add_to_cart.click()
            await self.page.wait_for_timeout(2000)
        except Exception as e:
            print(f"Error al añadir al carrito: {e}")