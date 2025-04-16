from playwright.async_api import Page
DELAY = 1000
MAX_ATTEMPTS = 1

class HomeToPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.searchIcon = self.page.locator(".nav-search > a:nth-child(1) > i:nth-child(1)")
        self.searchInput = self.page.locator("fieldset.text > input:nth-child(1)")
        self.newItems = self.page.locator(".discovery-new-item > a:nth-child(2)")
        self.superStore = self.page.locator(".btn-outline-dark")
        self.slkSeries = self.page.locator(".tf-sw-lookbook > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3)")
        self.motionPro = self.page.locator(".tf-sw-lookbook > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3)")
        self.ecomus = self.page.locator(".logo")
        self.franklinSiganture = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")
        self.quickAdd = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.quickAddFav = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2)")
        self.quickAddCompare = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3)")
        self.quickView = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(4)")
        self.closerQuick = self.page.locator("#quick_add > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
        self.closerCompare = self.page.locator(".close-popup")

    async def navigate(self, url: str) -> None:
        assert await self.page.goto(url, wait_until="domcontentloaded")
    
    async def closePopUpHome(self):
        await self.page.wait_for_timeout(2000)
        await self.popUpHome.click()

    async def closerQuickView(self):
        await self.page.wait_for_timeout(2000)
        await self.closerQuick.click()
    
    async def closerQuickCompare(self):
        await self.page.wait_for_timeout(2000)
        await self.closerCompare.click()
    
    async def productHoverAddCart(self):
        await self.closePopUpHome()
        await self.franklinSiganture.scroll_into_view_if_needed()
        await self.franklinSiganture.hover()
        await self.franklinSiganture.wait_for(state="visible")
        await self.quickAdd.click()
        await self.page.wait_for_timeout(1000)
    
    async def productHoverAddFav(self):
        await self.closePopUpHome()
        await self.franklinSiganture.scroll_into_view_if_needed()
        await self.franklinSiganture.hover()
        await self.franklinSiganture.wait_for(state="visible")
        await self.quickAddFav.click()
        await self.quickAddFav.hover()
        await self.page.wait_for_timeout(1000)

    async def productHoverAddCompare(self):
        await self.closePopUpHome()
        await self.franklinSiganture.scroll_into_view_if_needed()
        await self.franklinSiganture.hover()
        await self.franklinSiganture.wait_for(state="visible")
        await self.quickAddCompare.click()
        await self.page.wait_for_timeout(1000)

    async def productHoverView(self):
        await self.closePopUpHome()
        await self.franklinSiganture.scroll_into_view_if_needed()
        await self.franklinSiganture.hover()
        await self.franklinSiganture.wait_for(state="visible")
        await self.quickView.click()
        await self.page.wait_for_timeout(1000)
    
    async def click_newItems(self):
        await self.newItems.click()
        await self.page.wait_for_timeout(1000)
    
    async def click_superStore(self):
        await self.superStore.scroll_into_view_if_needed()
        await self.superStore.click()
        await self.page.wait_for_timeout(1000)
    
    async def click_slkSeries(self):
        await self.slkSeries.scroll_into_view_if_needed()
        await self.slkSeries.click()
        await self.page.wait_for_timeout(1000)
    
    async def click_motionPro(self):
        await self.motionPro.scroll_into_view_if_needed()
        await self.motionPro.click()
        await self.page.wait_for_timeout(1000)
    
    async def click_ecomus(self):
        await self.ecomus.click()
        await self.page.wait_for_timeout(1000)
    
    async def search_for_item(self, item: str):
        for attempt in range(MAX_ATTEMPTS):
            try:
                await self.searchIcon.click()
                await self.page.wait_for_timeout(1000)
                await self.searchInput.fill(item)
                return
            except Exception:
                if attempt < MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(DELAY)