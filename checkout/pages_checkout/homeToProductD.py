import time
from playwright.async_api import Page

class HomeToProductDetails:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHomePage = self.page.locator("span.btn-hide-popup")
        self.firstCollection = page.locator('a.collection-image.img-style').nth(0)
        self.firstProduct = page.locator('div.card-product-wrapper').nth(0)

    async def closePopup(self):
        assert self.popUpHomePage, "No popup found"
        await self.popUpHomePage.click()
        time.sleep(3)

    async def clickFirstCollection(self):
        assert self.firstCollection, "No collection found"
        await self.firstCollection.click()

    async def clickFirstProduct(self):
        assert self.firstProduct, "No product found"
        await self.firstProduct.click()