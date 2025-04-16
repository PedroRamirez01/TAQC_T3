from playwright.async_api import Page
DELAY = 1000
MAX_ATTEMPTS = 1

class FilterProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.filterBttn = self.page.locator(".tf-btn-filter")
        self.filterMen = self.page.locator("li.cate-item:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
        self.filterWomen = self.page.locator("li.cate-item:nth-child(3) > a:nth-child(1) > span:nth-child(1)")
        self.filterDenim = self.page.locator("li.cate-item:nth-child(4) > a:nth-child(1) > span:nth-child(1)")
        self.filterDress = self.page.locator("li.cate-item:nth-child(5) > a:nth-child(1) > span:nth-child(1)")
        self.closePopUp = self.page.locator(".offcanvas-backdrop")
        self.quickAdd = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.addToCart = self.page.locator("div.tf-product-info-buy-button:nth-child(4) > form:nth-child(1) > a:nth-child(1)")
        self.shopCategories = self.page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.outOfStockFilter = self.page.locator("#availability > ul:nth-child(1) > li:nth-child(2) > input:nth-child(1)")
        self.producto = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")
        self.avaliable = self.page.locator("#availability > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)")
        self.slider = self.page.locator("#slider")
        self.brand = self.page.locator("#brand > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)")
        self.color = self.page.locator("input.bg_brown")
        self.size = self.page.locator("#size > ul:nth-child(1) > li:nth-child(2) > input:nth-child(1)")
        self.clearFilter = self.page.locator("a.tf-btn:nth-child(4)")
        self.totalCart = None


    async def doFilter(self):
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUp.click()
        await self.filterBttn.click()
        await self.avaliable.click()
        await self.brand.click()
        await self.color.click()
        await self.size.click()
    
    async def clear_Filter(self):
        await self.filterBttn.click()
        await self.clearFilter.click()

    async def addCart(self):
        await self.producto.hover()
        await self.producto.wait_for(state="visible")
        await self.quickAdd.click()
        await self.addToCart.click()
        self.totalCart = self.page.locator(".tf-totals-total-value")
        await self.totalCart.wait_for(state="visible")
    
    async def totalCart_value(self):
        total_value = await self.totalCart.inner_text()
        return total_value

    async def outOfStock(self):
        await self.filterBttn.click()
        await self.outOfStockFilter.click()

    async def navigate(self, url: str) -> None: #Contenedor de la página
        await self.page.goto(url, wait_until="domcontentloaded")
    
    async def doFilterMen(self):
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUp.click()
    
    async def doFilterWomen(self):
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUp.click()
    
    async def doFilterDenim(self):
        await self.filterBttn.click()
        for attempy in range(MAX_ATTEMPTS):
            try:
                await self.filterDenim.click()
                return
            except Exception:
                if attempy < MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(DELAY)

    async def doFilterDress(self):
        await self.filterBttn.click()
        for attempy in range(MAX_ATTEMPTS):
            try:
                await self.filterDress.click()
                return
            except Exception:
                if attempy < MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(DELAY)

    async def PopUp(self):
        if await self.closePopUp.count() > 0 and await self.closePopUp.is_visible():
            await self.closePopUp.click()
            await self.page.wait_for_timeout(2000)
    
    async def takeScreenshot(self, path, fullPage=False):
        await self.page.screenshot(path=path, full_page=fullPage)
    

    """Flujos optimizados para el test de pytest"""
    # Test de clearFilter
    async def clearFilterStep1(self):
        await self.filterBttn.click()
        await self.outOfStockFilter.click()
        await self.closePopUp.click()
    
    # Test de clearFilter
    async def clearFilterStep2(self):
        await self.clear_Filter()
        await self.PopUp()

    # Test de Denim
    async def filterNotWorkingDenim(self):
        await self.doFilterDenim()
        await self.PopUp()

    # Test de Dress
    async def filterNotWorkingDress(self):
        await self.doFilterDress()
        await self.PopUp()
    
    # Test de filter Out of stock
    async def outOfStockFlow(self):
        await self.outOfStock()
        await self.PopUp()
        await self.addCart()
