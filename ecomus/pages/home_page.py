from playwright.async_api import Page, expect
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
    """

    def __init__(self, page: Page):
        self.page = page
        self.url = Config.URL_BASE
        self.popUpHome = self.page.locator("span.btn-hide-popup")
        self.searchIcon = self.page.locator(".nav-search > a:nth-child(1) > i:nth-child(1)")
        self.searchInput = self.page.locator("fieldset.text > input:nth-child(1)")
        self.fashionSearch = page.locator("li.tf-quicklink-item:nth-child(1) > a:nth-child(1)")
        self.ecomus = self.page.locator("#header > div > div > div.col-xl-3.col-md-4.col-6 > a")
        self.products = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")
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

    async def navigate(self) -> None:
        """
        Navigates to the base URL of the Ecomus website.
        
        Loads the home page and verifies that the correct URL is reached.
        Uses 'domcontentloaded' event to ensure the page is ready for interaction.
        """
        await self.page.goto(self.url, wait_until="domcontentloaded")
        await expect(self.page).to_have_url(self.url)
    
    async def fashion_search(self):
        """
        Clicks on the fashion category search link.
        
        Waits for 2 seconds to ensure the page is stable before clicking on the
        fashion category quick link to filter products by fashion category.
        """
        await self.page.wait_for_timeout(2000)
        await self.fashionSearch.click()
    
    async def hover_product_and_quick_add(self):
        """
        Performs the hover and quick add workflow for the first product.
        
        Scrolls to make the product visible, hovers over it to reveal quick actions,
        verifies that the quick add popup content is visible, and clicks
        the quick add button to add the product to cart.
        """
        await self.products.scroll_into_view_if_needed()
        await self.products.wait_for(state="visible")
        await self.products.hover()
        await expect(self.quickAddPopupContent).to_be_visible()
        await self.quickAdd.click()
        
    async def close_pop_up_home(self) -> None:
        """
        Handles the newsletter popup on the home page.
        
        Waits for the popup to be visible, ensures all network activity is complete,
        clicks the close button, and verifies that the popup is properly hidden.
        This improves test reliability by ensuring popups don't interfere with subsequent actions.
        """
        await self.popUpHome.wait_for(state="visible")
        await expect(self.popUpHome).to_be_visible()
        await self.page.wait_for_timeout(1000)
        #await self.page.wait_for_load_state("networkidle")
        await self.popUpHome.click()
        #await expect(self.popUpHome).to_be_hidden()

    async def closer_quick_view(self) -> None:
        """
        Closes the quick view product popup.
        
        Waits for 2 seconds to ensure the popup is fully loaded before
        clicking the close button to dismiss the quick view dialog.
        """
        await self.page.wait_for_timeout(2000)
        await self.closerQuick.click()
    
    async def click_ecomus(self) -> None:
        """
        Clicks on the Ecomus logo to return to the home page.
        
        Simulates clicking on the site logo (a common navigation pattern)
        and waits for 1 second for navigation to complete.
        """
        await self.ecomus.click()
        await self.page.wait_for_timeout(1000)

    async def search_icon_click(self) -> str:
        """
        Clicks on the search icon to open the search interface.
        
        Clicks the search icon in the navigation bar and waits for 1 second
        for the search input to appear.
        
        Returns:
            str: The current page URL after clicking the search icon
        """
        await self.searchIcon.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def search_input_fill(self, item: str = "Paddle") -> str:
        """
        Enters a search term into the search input field.
        
        Fills the search input with the specified term (defaults to "Paddle")
        and waits for 1 second for search results to update.
        
        Args:
            item (str, optional): The search term to enter. Defaults to "Paddle".
            
        Returns:
            str: The current page URL after entering the search term
        """
        await self.searchInput.fill(item)
        await self.page.wait_for_timeout(1000)
        return self.page.url

    # Main Flows
    
    async def search_for_item(self) -> str:
        """
        Executes the complete search workflow with retry mechanism.
        
        Attempts to perform a search operation multiple times if needed:
        1. Closes any popup that might be visible
        2. Clicks on the search icon to open the search box
        3. Enters the default search term
        4. Collects and returns URLs at different stages of the search process
        
        Includes error handling with configurable retry attempts and delays.
        
        Returns:
            list: A list containing URLs at different stages of the search process
        """
        urls = []
        for attempt in range(Config.MAX_ATTEMPTS):
            try:
                await self.close_pop_up_home()
                url1 = await self.search_icon_click()
                if url1:
                    urls.append(url1)
                await self.page.wait_for_timeout(1000)

                url2 = await self.search_input_fill()
                if url2:
                    urls.append(url2)

                return urls
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < Config.MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(Config.DELAY)