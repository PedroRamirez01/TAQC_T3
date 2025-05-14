from playwright.async_api import Page ,expect
from config.config import Config

class HomeToPage:
    """
    This class implements the Page Object Model pattern for the Ecomus website's home page.
    It provides methods to interact with key elements such as:

    Navigation buttons and category links
    Search functionality
    Quick actions (Add to cart, add to favorites, compare)
    Product discovery features
    Popup management

    Main Features:

    Category navigation (Clothing, Paddles, Accessories, Men)
    Product search and filtering
    Quick view and add-to-cart functionality
    Wishlist and product comparison features
    Discovery sections (New Arrivals, Super Store, SLK Series, Motion Pro)

    Main Flows:

    search_for_item: Performs product search using the search icon and input field
    navigate_and_collect_discovery_urls: Navigates through featured sections and collects URLs
    navigate_and_collect_category_urls: Navigates through main categories and collects URLs
    hover_product_and_quick_add: Adds a product to the cart using a quick action
    hover_product_and_add_fav: Adds a product to favorites using a quick action
    hover_product_and_add_compare: Adds a product to the comparison list using a quick action
    hover_product_and_view: Displays a quick view of the product
    """

    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("#newsletterPopup span.btn-hide-popup")
        self.searchIcon = self.page.locator(".nav-search > a:nth-child(1) > i:nth-child(1)")
        self.searchInput = self.page.locator("fieldset.text > input:nth-child(1)")
        self.fashionSearch = page.locator("li.tf-quicklink-item:nth-child(1) > a:nth-child(1)")
        self.ecomus = self.page.locator(".logo")
        self.franklinSiganture = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")
        self.quickAdd = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.quickAddFav = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2)")
        self.quickAddCompare = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3)")
        self.quickView = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(4)")
        self.closerQuick = self.page.locator("#quick_add > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
        self.closerCompare = self.page.locator(".close-popup")
        self.quickAddPopupContent = page.locator("#quick_add > div:nth-child(1) > div:nth-child(1)")
        self.quickAddFavPopupContent = page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > span:nth-child(2)")
        self.quickAddComparePopupContent = page.locator("#compare > div:nth-child(1) > div:nth-child(2)")
        self.quickViewPopupContent = page.locator("div.tf-product-info-list:nth-child(1)")

    async def navigate(self, url: str) -> None:
        await self.page.goto(url, wait_until="domcontentloaded")
        await expect(self.page).to_have_url(url)
    
    async def fashion_search(self):
        await self.page.wait_for_timeout(2000)
        await self.fashionSearch.click()
    
    async def close_pop_up_home(self):
        await expect(self.popUpHome).to_be_visible()
        await self.page.wait_for_load_state("networkidle")
        await self.popUpHome.click()
        await expect(self.popUpHome).to_be_hidden()

    async def closer_quick_view(self):
        await self.page.wait_for_timeout(2000)
        await self.closerQuick.click()
    
    async def click_ecomus(self):
        await self.ecomus.click()
        await self.page.wait_for_timeout(1000)

    async def search_icon_click(self):
        await self.searchIcon.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def search_input_fill(self, item: str = "Paddle"):
        await self.searchInput.fill(item)
        await self.page.wait_for_timeout(1000)
        return self.page.url

    # Main Flows
    
    async def search_for_item(self):
        urls = []
        for attempt in range(Config.MAX_ATTEMPTS):
            try:
                await self.close_pop_up_home()
                url1 = await self.search_icon_click()
                if url1: urls.append(url1)
                await self.page.wait_for_timeout(1000)

                url2 = await self.search_input_fill()
                if url2: urls.append(url2)

                return urls
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < Config.MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(Config.DELAY)