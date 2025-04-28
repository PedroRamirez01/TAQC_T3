from playwright.async_api import Page
from config.config import Config

class ProductDetailPage:
    """
    Class that represents the product detail page on the test website.
    Provides methods for interacting with page elements and performing actions such as
    navigating to the page, adding products to the cart, and checking discounts.
    Attributes:
        url (str): URL of the product detail page.
        page (Page): Instance of the Playwright page.
        title (Locator): Locator for the product title.
        price (Locator): Locator for the product price.
        discount (Locator): Locator for the product discount.
        price_on_sale (Locator): Locator for the product's sale price.
        span_color (Locator): Locator for the product's color.
        checked_input (Locator): Locator for the selected color input.
        span_size (Locator): Locator for the product's size.
        size_selected (Locator): Locator for the selected size.
        input_quantity (Locator): Locator for the product quantity.
        add_to_cart (Locator): Locator for the "Add to Cart" button.
        buy_with_btn (Locator): Locator for the "Buy with Button" button.
        cart_add_btn (Locator): Locator for the "Add to Cart" button in the popup.
        cart_input (Locator): Locator for the quantity input in the cart popup.
        cart_close (Locator): Locator for closing the cart popup.
        shipping_text (Locator): Locator for the free shipping text in the cart popup.
    Methods:
        navigate(): Navigates to the product detail page.
        press_cart(): Presses the "Add to Cart" button.
        cart_add_product(quantity: int): Adds a product to the cart with the specified quantity.
        verify_free_shipping(quantity: int): Checks if free shipping is applied after adding products to the cart.
        cart_add_cart(quantity: int): Checks if the cart quantity is updated correctly after adding products.
        verify_discount(): Checks if the discount is applied correctly.
        add_to_cart_with_input(quantity: int): Adds a product to the cart using a quantity input field.
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
            print(f"Error adding to cart: {e}")
            return False
