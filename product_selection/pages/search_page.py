from playwright.async_api import Page

class HomeToSearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.searchIcon = self.page.locator(".nav-search > a:nth-child(1) > i:nth-child(1)")
        self.searchInput = self.page.locator("fieldset.text > input:nth-child(1)")

    async def navigate(self, url: str) -> None: #Contenedor de la página
        assert await self.page.goto(url, wait_until="domcontentloaded")

    async def closePopUpHomePage(self):
        self.popUpHome, "Pop-up is not found"
        await self.popUpHome.click()
        await self.page.wait_for_timeout(2000)
    
    async def searchIcons(self):
        await self.searchIcon.click()
        await self.page.wait_for_timeout(2000)

    async def search_for_item(self, item: str, max_attempts: int, delay: int):
        for attempt in range(max_attempts):
            try:
                await self.searchInput.fill(item)
                return
            except Exception:
                if attempt < max_attempts - 1:
                    await self.page.wait_for_timeout(delay)