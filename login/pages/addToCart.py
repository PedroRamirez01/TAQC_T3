from playwright.async_api import Page

class AddToCart:

    """
    This class is used to interact with the add to cart page of the website.
    It contains methods to change the color and size of the product, increment and decrement the quantity, and add the product to the cart.
    atributes:
    - page: The page object of the website.
    - changeColorButton: The button to change the color of the product.
    - changeSizeButton: The button to change the size of the product.
    - IncrementButton: The button to increment the quantity of the product.
    - DecrementButton: The button to decrement the quantity of the product
    - addToCartButton: The button to add the product to the cart.

    methods:
    - changeColor: This method is used to change the color of the product.
    - changeSize: This method is used to change the size of the product.    
    - incrementQuantity: This method is used to increment the quantity of the product.
    - decrementQuantity: This method is used to decrement the quantity of the product.
    - addToCart: This method is used to add the product to the cart.
    """
    
    def __init__(self, page: Page):
        self.page = page
        self.changeColorButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker > div:nth-child(1) > form > label:nth-child(4)')
        self.changeSizeButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker > div:nth-child(2) > form > label:nth-child(6)')
        self.IncrementButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.plus-btn')
        self.DecrementButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.minus-btn')
        self.addToCartButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > a.tf-btn.btn-fill.justify-content-center.fw-6.fs-16.flex-grow-1.animate-hover-btn')

    async def changeColor(self):
        assert self.changeColorButton, "No color button found"
        await self.changeColorButton.click()

    async def changeSize(self):
        assert self.changeSizeButton, "No size button found"
        await self.changeSizeButton.click()

    async def incrementQuantity(self):
        assert self.IncrementButton, "No increment button found"
        await self.IncrementButton.click()

    async def decrementQuantity(self):
        assert self.DecrementButton, "No decrement button found"
        await self.DecrementButton.click()

    async def addToCart(self):
        assert self.addToCartButton, "No add to cart button found"
        await self.addToCartButton.click()
        