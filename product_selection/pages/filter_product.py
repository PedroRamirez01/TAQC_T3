import time
from playwright.async_api import Page

class FilterProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.searchIcon = self.page.locator(".nav-search > a:nth-child(1) > i:nth-child(1)")
        self.quickLink = page.locator("li.tf-quicklink-item:nth-child(1) > a:nth-child(1)")
        self.filterBttn = page.locator(".tf-btn-filter")
        self.filterMen = page.locator("li.cate-item:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
        self.filterWomen = page.locator("li.cate-item:nth-child(3) > a:nth-child(1) > span:nth-child(1)")
        self.closePopUp = page.locator(".offcanvas-backdrop")

    async def searchForItem(self):
        await self.searchIcon.click()

    async def qckLink(self):
        assert self.quickLink, "Quick link is not found"
        await self.quickLink.click()
    
    async def doFilterMen(self):
        assert self.filterBttn, "Filter button is not found"
        await self.filterBttn.click()
        await self.filterMen.click()
    
    async def doFilterWomen(self):
        assert self.filterBttn, "Filter button is not found"
        await self.filterBttn.click()
        await self.filterWomen.click()
    
    async def PopUp(self):
        await self.closePopUp.click()
        time.sleep(3)
    
    async def takeScreenshot(self, path, fullPage=False):
        await self.page.screenshot(path=path, full_page=fullPage)