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
        self.changeColorButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker > div:nth-child(1) > form > label:nth-child(4)')
        self.changeSizeButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-variant-picker > div:nth-child(2) > form > label:nth-child(6)')
        self.IncrementButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.plus-btn')
        self.DecrementButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-quantity > div.wg-quantity > span.btn-quantity.minus-btn')
        self.addToCartButton = self.page.locator('#wrapper > section:nth-child(3) > div.tf-main-product.section-image-zoom > div > div > div:nth-child(2) > div > div.tf-product-info-list.other-image-zoom > div.tf-product-info-buy-button > form > a.tf-btn.btn-fill.justify-content-center.fw-6.fs-16.flex-grow-1.animate-hover-btn')
        self.clickFirstPaddleButton = self.page.locator('#wrapper > div > section:nth-child(6) > div.tf-grid-layout.tf-col-2.md-col-3.gap-0.home-pckaleball-page > div:nth-child(1) > div.card-product-wrapper > a > img.lazyload.img-hover')
        self.closeModalButton = self.page.locator('#newsletterPopup > div > div > div.modal-top > span')
        self.cartButton = self.page.locator('#header > div > div > div.col-xxl-5.col-md-4.col-3 > ul > li.nav-cart > a')

    async def navigate(self, url: str) -> None:
        """
        Navega a la URL especificada y espera a que el DOM esté cargado.
        :param url: URL de destino.
        """
        await self.page.goto(url, wait_until="domcontentloaded")

    async def changeColor(self):
        """
        Changes the product color.
        """
        await expect(self.changeColorButton).to_be_visible()
        await self.changeColorButton.click()

    async def changeSize(self):
        """
        Changes the product size.
        """
        await expect(self.changeSizeButton).to_be_visible()
        await self.changeSizeButton.click()

    async def incrementQuantity(self):
        """
        Increases the product quantity.
        """
        await expect(self.IncrementButton).to_be_visible()
        await self.IncrementButton.click()

    async def decrementQuantity(self):
        """
        Decreases the product quantity.
        """
        await expect(self.DecrementButton).to_be_visible()
        await self.DecrementButton.click()

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
