from playwright.async_api import Page

class FilterProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.filterBttn = self.page.locator(".tf-btn-filter")
        self.filterMen = self.page.locator("li.cate-item:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
        self.filterWomen = self.page.locator("li.cate-item:nth-child(3) > a:nth-child(1) > span:nth-child(1)")
        self.closePopUp = self.page.locator(".offcanvas-backdrop")
        self.shopCategories = self.page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.div1 = None
        self.div2 = None
        self.div3 = None
    
    async def closePopUpHomePage(self):
        self.popUpHome, "Pop-up is not found"
        await self.popUpHome.click()
        await self.page.wait_for_timeout(2000)

    async def navigate(self, url: str) -> None: #Contenedor de la página
        await self.page.goto(url, wait_until="domcontentloaded")
    
    async def doFilterMen(self):
        assert self.filterBttn, "Filter button is not found"
        await self.filterBttn.click()
        await self.filterMen.click()
        self.div1 = self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        await self.div1.wait_for(state="visible")
    
    async def doFilterWomen(self):
        assert self.filterBttn, "Filter button is not found"
        await self.filterBttn.click()
        await self.filterWomen.click()
        self.div2 = self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        await self.div2.wait_for(state="visible")
    
    async def shopByCategories(self):
        assert self.shopCategories, "Shop by categories is not found"
        await self.shopCategories.click()
        self.div3 = self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        await self.div3.wait_for(state="visible")
    
    async def PopUp(self):
        if await self.closePopUp.count() > 0 and await self.closePopUp.is_visible():
            await self.closePopUp.click()
            await self.page.wait_for_timeout(2000)
    
    async def takeScreenshot(self, path, fullPage=False):
        await self.page.screenshot(path=path, full_page=fullPage)

    async def compare_div(self):
        assert self.div1 is not None, "div1 is not found"
        assert self.div2 is not None, "div2 is not found"
        assert self.div3 is not None, "div3 is not found"

        div1_text = await self.div1.inner_text()
        div2_text = await self.div2.inner_text()
        div3_text = await self.div3.inner_text()

        #print(f"Div1 Text in Test: {div1_text}")
        #print(f"Div2 Text in Test: {div2_text}")
        #print(f"Div3 Text in Test: {div3_text}")

        if div1_text == div2_text and div1_text == div3_text:
            return True
        else:
            return False
