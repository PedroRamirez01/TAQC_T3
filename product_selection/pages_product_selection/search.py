import time
from playwright.async_api import Page

class HomeToSearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.searchIcon = self.page.locator(".nav-search > a:nth-child(1) > i:nth-child(1)")
        self.searchInput = self.page.locator("fieldset.text > input:nth-child(1)")
    
    async def closePopUpHomePage(self):
        assert self.popUpHome, "Pop-up is not found"
        await self.popUpHome.click()

    async def search_for_item(self, item: str):
        await self.searchIcon.click()
        await self.searchInput.fill(item)
        await self.searchIcon.click() , "Search icon is not working"