from playwright.async_api import Page, expect

class AddToCart:

    """
    Page Object Model for the add-to-cart page.
    Allows changing product color and size, modifying quantity, and adding products to the cart.
    """
    
    def __init__(self, page: Page):
        """
        Initializes locators for the add-to-cart functionalities.
        :param page: Instance of Playwright Page.
        """
        self.page = page
        self.changeColorButton = '.tf-product-info-list.other-image-zoom .tf-product-info-variant-picker form.variant-picker-values label:has(span.tooltip:has-text("{color}"))'
        self.changeSizeButton = '#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker form > label:has-text("{size}")'
        self.incrementButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.plus-btn')
        self.decrementButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.minus-btn')
        self.addToCartButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > a.tf-btn.btn-fill.justify-content-center.fw-6.fs-16.flex-grow-1.animate-hover-btn')
        self.quantityInput = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > input[type=text]')
        self.clickFirstPaddleButton = self.page.locator('#wrapper > div > section:nth-child(6) > div.tf-grid-layout.tf-col-2.md-col-3.gap-0.home-pckaleball-page > div:nth-child(1) > div.card-product-wrapper > a > img.lazyload.img-hover')
        self.clickThirdPaddleButton = self.page.locator('#wrapper > div > section:nth-child(6) > div.tf-grid-layout.tf-col-2.md-col-3.gap-0.home-pckaleball-page > div:nth-child(3) > div.card-product-wrapper > a > img.lazyload.img-hover')
        self.closeModalButton = self.page.locator('#newsletterPopup > div > div > div.modal-top > span')
        self.cartButton = self.page.locator('#header > div > div > div.col-xxl-5.col-md-4.col-3 > ul > li.nav-cart > a')
        self.closeCartButton = self.page.locator('#shoppingCart > div > div > div.header > span')

    async def navigate(self, url: str) -> None:
        """
        Navigates to the specified URL and waits for the DOM to be loaded.
        :param url: Target URL.
        """
        await self.page.goto(url, wait_until="domcontentloaded")

    async def changeColor(self, color: str):
        """
        Select a color for the product.
        :param color: Color to be selected.
        """
        color_locator = self.page.locator(self.changeColorButton.format(color=color))
        await self.page.mouse.move(0, 0)
        await expect(color_locator).to_be_visible()
        await color_locator.first.click()

    async def changeSize(self, size: str):
        """
        Change the size of the product.
        :param size: Size to be selected.
        """
        size_locator = self.page.locator(self.changeSizeButton.format(size=size))
        await expect(size_locator).to_be_visible()
        await size_locator.click()

    async def incrementQuantity(self):
        """
        Increases the product quantity.
        """
        await expect(self.incrementButton).to_be_visible()
        await self.incrementButton.click()

    async def decrementQuantity(self):
        """
        Decreases the product quantity.
        """
        await expect(self.decrementButton).to_be_visible()
        await self.decrementButton.click()

    async def setItemQuantity(self, amount: int):
        await expect(self.quantityInput).to_be_visible()
        await self.quantityInput.fill(str(amount))

    async def addToCart(self):
        """
        Adds the product to the shopping cart.
        """
        await expect(self.addToCartButton).to_be_visible()
        await self.addToCartButton.click()

    async def performAddToCartActions(self):
        """
        Performs a series of actions to add a product to the cart.
        """
        await self.changeColor()
        await self.changeSize()
        await self.incrementQuantity()
        await self.incrementQuantity()
        await self.incrementQuantity()
        await self.incrementQuantity()
        await self.incrementQuantity() 
        await self.decrementQuantity()
        await self.addToCart()

    async def clickFirstPaddle(self):
        """
        Clicks on the first paddle in the product list.
        """
        await expect(self.clickFirstPaddleButton).to_be_visible()
        await self.clickFirstPaddleButton.click()

    async def clickThirdPaddle(self):
        """
        Clicks on the third paddle in the product list.
        """
        await expect(self.clickThirdPaddleButton).to_be_visible()
        await self.clickThirdPaddleButton.click()

    async def closeModal(self):
        """
        Closes the modal if it is open.
        """
        await expect(self.closeModalButton).to_be_visible()
        await self.closeModalButton.click()

    async def clickCartButton(self):
        """
        Clicks on the cart button.
        """
        await expect(self.cartButton).to_be_visible()
        await self.cartButton.click()

    async def closeCart(self):
        """
        Closes the cart.
        """
        await expect(self.closeCartButton).to_be_visible()
        await self.closeCartButton.click()
