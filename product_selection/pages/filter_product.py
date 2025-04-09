from playwright.async_api import Page

class FilterProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.searchIcon = self.page.locator(".nav-search > a:nth-child(1) > i:nth-child(1)")
        self.quickLink = page.locator("li.tf-quicklink-item:nth-child(1) > a:nth-child(1)")
        self.filterBttn = page.locator(".tf-btn-filter")
        self.filterMen = page.locator("li.cate-item:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
        self.filterWomen = page.locator("li.cate-item:nth-child(3) > a:nth-child(1) > span:nth-child(1)")
        self.closePopUp = page.locator(".offcanvas-backdrop")
        self.div1 = None
        self.div2 = None
    
    async def closePopUpHomePage(self):
        self.popUpHome, "Pop-up is not found"
        await self.popUpHome.click()
        await self.page.wait_for_timeout(2000)

    async def navigate(self, url: str) -> None: #Contenedor de la página
        await self.page.goto(url, wait_until="domcontentloaded")

    async def searchForItem(self):
        await self.searchIcon.click()

    async def qckLink(self):
        assert self.quickLink, "Quick link is not found"
        await self.quickLink.click()
    
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
    
    async def PopUp(self):
        if await self.closePopUp.count() > 0 and await self.closePopUp.is_visible():
            await self.closePopUp.click()
            await self.page.wait_for_timeout(2000)
    
    async def takeScreenshot(self, path, fullPage=False):
        await self.page.screenshot(path=path, full_page=fullPage)

    async def compare_div(self):
        assert self.div1 is not None, "div1 is not found"
        assert self.div2 is not None, "div2 is not found"

        assert await self.div1.count() > 0, "div1 no existe en la página"
        assert await self.div2.count() > 0, "div2 no existe en la página"

        div1_text = await self.div1.inner_text()
        div2_text = await self.div2.inner_text()

        if div1_text == div2_text:
            print("Los divs son iguales")
            print(f"Texto de div1: {div1_text}")
            print(f"Texto de div2: {div2_text}")
            return True
        else:
            print("Los divs son diferentes")
            print(f"Texto de div1: {div1_text}")
            print(f"Texto de div2: {div2_text}")
            return False