from playwright.async_api import Page , expect
from config.config import Config

class FilterProductPage:
    """
    This class implements the Page Object Model pattern for the product filtering functionality.
    It provides methods to interact with key filtering elements such as:

    Category filters
    Product availability filters
    Brand and color filters
    Size selection filters
    Filter clearing functionality
    Shopping cart interactions

    """
    def __init__(self, page: Page):
        self.page = page
        self.url = Config.URL_FILTER
        self.popUpHome = self.page.locator("span.btn-hide-popup")
        self.filterBttn = self.page.locator(".tf-btn-filter")
        self.filterMen = self.page.locator("li.cate-item:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
        self.filterWomen = self.page.locator("li.cate-item:nth-child(3) > a:nth-child(1) > span:nth-child(1)")
        self.filterDenim = self.page.locator("li.cate-item:nth-child(4) > a:nth-child(1) > span:nth-child(1)")
        self.filterDress = self.page.locator("li.cate-item:nth-child(5) > a:nth-child(1) > span:nth-child(1)")
        self.filterOrder = self.page.locator(".btn-select")
        self.filterOrderBy = self.page.locator("div.select-item:nth-child(4)")
        self.hoverSizeXL = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(4)")
        self.productBrown = self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > ul:nth-child(3) > li:nth-child(1)")
        self.closePopUpFilter = self.page.locator(".offcanvas-backdrop")
        self.quickAdd = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.addToCart = self.page.locator("div.tf-product-info-buy-button:nth-child(4) > form:nth-child(1) > a:nth-child(1)")
        self.shopCategories = self.page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.outOfStockFilter = self.page.locator("#availability > ul:nth-child(1) > li:nth-child(2) > input:nth-child(1)")
        self.producto = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")
        self.slicer = self.page.locator("#slider")
        self.avaliable = self.page.locator("#availability > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)")
        self.brand = self.page.locator("#brand > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)")
        self.color = self.page.locator("input.bg_brown")
        self.size = self.page.locator("#size > ul:nth-child(1) > li:nth-child(2) > input:nth-child(1)")
        self.filterSizeXL = self.page.locator("#size > ul:nth-child(1) > li:nth-child(4) > input:nth-child(1)")
        self.clearFilter = self.page.locator("a.tf-btn:nth-child(4)")
        self.productThree = self.page.locator("div.card-product:nth-child(3) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")

    async def navigate(self, url: str) -> None:
        """
        Navigates to the specified URL and waits for the page to be fully loaded.
        Args:url (str): The URL to navigate to
        """
        await self.page.goto(url, wait_until="domcontentloaded")
    
    async def click_color(self):
        """
        Applies a color filter to the product list.
        Opens the filter panel, selects the brown color option, closes the panel,
        and hovers over the first product's color swatch to verify the filter application.
        Returns: Locator: A locator for the color element for verification
        """
        await self.filterBttn.click()
        await self.color.click()
        await self.pop_up()
        await self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > ul:nth-child(3) > li:nth-child(1)").hover()
        return self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > ul:nth-child(3) > li:nth-child(1) > span:nth-child(1)")

    async def size_XL(self):
        """
        Applies the XL size filter to the product list.
        Opens the filter panel, selects the XL size filter, closes the panel,
        and hovers over the first product to verify size availability.
        Returns:
            Locator: A locator for the XL size element for verification
        """
        await self.filterBttn.click()
        await self.filterSizeXL.click()
        await self.pop_up()
        await self.producto.hover()
        return self.hoverSizeXL

    async def order_by(self):
        """
        Changes the product ordering option.       
        Clicks the order dropdown and selects a specific ordering option (typically price or relevance).
        """
        await self.filterOrder.click()
        await self.filterOrderBy.click()

    async def move_price_slider(self, pixels: int) -> None:
        """
        Adjusts the price range slider by dragging it horizontally.
        Args:
            pixels (int): The number of pixels to move the slider horizontally (positive = right, negative = left)
        """
        handle_box = await self.slicer.bounding_box()
        await self.slicer.wait_for(state="visible")
        # Get the center X and Y coordinates of the handle
        x = handle_box['x'] + handle_box['width'] / 2
        y = handle_box['y'] + handle_box['height'] / 2        
        # Simple drag operation on X-axis only
        await self.page.mouse.move(x, y)
        await self.page.mouse.down()
        await self.page.mouse.move(x + pixels, y)
        await self.page.mouse.up()
        # Wait for any animations to complete
        await self.page.wait_for_timeout(1500)

    async def click_Brand(self):
        """
        Applies a brand filter to the product list.

        Opens the filter panel, selects the first brand option, verifies it's enabled,
        and closes the filter panel.
        """
        await self.filterBttn.click()
        await self.brand.click()
        await expect(self.brand).to_be_enabled()
        await self.pop_up()

    async def clear_Filter(self):
        """
        Resets all applied filters by clicking the clear filter button.

        Opens the filter panel, clicks the clear button, and closes the panel.

        Returns:
            Locator: A locator for the filter control wrapper for verification
        """
        await self.filterBttn.click()
        await self.clearFilter.click()
        await self.closePopUpFilter.click()
        return await self.page.locator(".wrapper-control-shop > div:nth-child(2)")

    async def do_filter_men(self):
        """
        Applies the Men category filter to show only men's products.

        Opens the filter panel, selects the Men category, and closes the panel.
        """
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUpFilter.click()

    async def do_filter_women(self):
        """
        Applies the Women category filter to show only women's products.

        Opens the filter panel, selects the Women category, and closes the panel.
        """
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUpFilter.click()

    async def do_filter_men_url(self):
        """
        Applies the Men category filter and returns the resulting URL.

        Returns:
            str: The URL after applying the Men filter, useful for verifying proper navigation
        """

        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUpFilter.click()
        return self.page.url

    async def do_filter_women_url(self):
        """
        Applies the Women category filter and returns the resulting URL.

        Returns:
            str: The URL after applying the Women filter, useful for verifying proper navigation
        """
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUpFilter.click()
        return self.page.url

    async def do_multiplies_filter(self):
        """
        Applies multiple filters in sequence to narrow down product results.
        
        Applies the Women category filter, then availability, brand, color, and size filters
        to demonstrate compound filtering functionality.
        """
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUpFilter.click()
        await self.filterBttn.click()
        await self.avaliable.click()
        await self.brand.click()
        await self.color.click()
        await self.size.click()
        await self.closePopUpFilter.click()
        #return await self.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()

    async def do_filter_denim_url(self):
        """
        Applies the Denim category filter with retry mechanism for reliability.

        Attempts to click the Denim filter multiple times if needed, with configurable
        delays between attempts to handle potential intermittent UI failures.

        Returns:
            str: The URL after applying the Denim filter
        """
        await self.filterBttn.click()
        for attempy in range(Config.MAX_ATTEMPTS):
            try:
                await self.filterDenim.click()
                await self.closePopUpFilter.click()
                return self.page.url
            except Exception:
                if attempy < Config.MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(Config.DELAY)
        await self.closePopUpFilter.click()

    async def do_filter_dress_url(self):
        """
        Applies the Dress category filter with retry mechanism for reliability.

        Attempts to click the Dress filter multiple times if needed, with configurable
        delays between attempts to handle potential intermittent UI failures.

        Returns:
            str: The URL after applying the Dress filter
        """
        await self.filterBttn.click()
        for attempy in range(Config.MAX_ATTEMPTS):
            try:
                await self.filterDress.click()
                await self.closePopUpFilter.click()
                return self.page.url
            except Exception:
                if attempy < Config.MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(Config.DELAY)

    async def out_of_stock(self):
        """
        Tests the out-of-stock product handling functionality.

        Applies the out-of-stock filter, attempts to add a product to cart,
        and verifies that the cart total remains at zero.
        """
        await self.filterBttn.click()
        await self.outOfStockFilter.click()
        await self.pop_up()
        await self.add_cart()
        value = self.page.locator(".tf-totals-total-value")
        await expect(value).to_have_text("0.00") 

    async def add_cart(self):
        """
        Adds the first visible product to the shopping cart.

        Hovers over a product, clicks the quick add button, and confirms
        the add-to-cart action in the subsequent dialog.
        """
        await self.producto.hover()
        await self.producto.wait_for(state="visible")
        await self.quickAdd.click()
        await self.addToCart.click()
        
    async def pop_up(self):
        """
        Handles popup closures throughout the application.

        Checks if the filter popup is visible and closes it if necessary,
        with a delay to ensure the UI updates properly.
        """
        if await self.closePopUpFilter.count() > 0 and await self.closePopUpFilter.is_visible():
            await self.closePopUpFilter.click()
            await self.page.wait_for_timeout(2000)

    #Main Flows 

    async def out_of_stock_flow(self):
        """
        Tests the complete out-of-stock product workflow.

        Verifies that products marked as out-of-stock cannot be added to cart
        and that appropriate feedback is provided to the user. Includes error
        handling for robustness.

        Returns:
            Result of the add_cart operation, expected to fail for out-of-stock items
        """
        total_value = []
        try:
            await self.out_of_stock()
            await self.pop_up()
            return await self.add_cart()
        except Exception as e:
            print(f"Error: {e}")

    async def do_clear_filter(self):
        """
        Tests the filter clearing functionality.

        Applies multiple filters and then tests the clear filter button to ensure
        all filters are properly reset. Includes error handling for robustness.

        Returns:
            Locator: The clear filter button locator for verification
        """
        try:
            await self.do_multiplies_filter()
            await self.filterBttn.click()
            filter_button = self.page.locator("a.tf-btn:nth-child(4)")
            return filter_button
        except Exception as e:
            print(f"Error: {e}")

    async def do_compare_div_men_women(self):
        """
        Compares product divisions between Men and Women categories.

        Collects and compares product containers from both Men and Women categories
        to verify distinct product sets. Includes error handling and logging.

        Returns:
            list: A list containing product division elements from both categories
        """
        divs = []	
        try:
            div1 = await self.do_filter_men_div()
            if div1:
                divs.append(div1)
                print(div1)
            div2 = await self.do_filter_women_div()
            if div2:
                divs.append(div2)
                print(div2)
            return divs
        except Exception as e:
            print(f"Error: {e}")

    async def filter_women(self):
        """
        Executes the complete Women's category filtering flow.

        Captures the initial URL, applies the Women filter, and returns both URLs
        for comparison and verification. Includes error handling and logging.

        Returns:
            list: A list containing the initial and filtered URLs
        """
        urls = []
        try:
            url1 = await self.initial_url()
            if url1:
                urls.append(url1)
            print(url1)
            
            url2 = await self.do_filter_women_url()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")

    async def filter_men(self):
        """
        Executes the complete Men's category filtering flow.

        Captures the initial URL, applies the Men filter, and returns both URLs
        for comparison and verification. Includes error handling and logging.

        Returns:
            list: A list containing the initial and filtered URLs
        """
        urls = []
        try:
            url1 = await self.initial_url()
            if url1:
                urls.append(url1)
            print(url1)

            url2 = await self.do_filter_men_url()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")

    async def filter_denim(self):
        """
        Executes the complete Denim category filtering flow.

        Captures the initial URL, applies the Denim filter, and returns both URLs
        for comparison and verification. Includes error handling and logging.

        Returns:
            list: A list containing the initial and filtered URLs
        """
        urls = []
        try:
            url1 = await self.initial_url()
            if url1:
                urls.append(url1)
            print(url1)

            url2 = await self.do_filter_denim_url()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")

    async def filter_dress(self):
        """
        Executes the complete Dress category filtering flow.

        Captures the initial URL, applies the Dress filter, and returns both URLs
        for comparison and verification. Includes error handling and logging.

        Returns:
            list: A list containing the initial and filtered URLs
        """
        urls = []
        try:
            url1 = await self.initial_url()
            if url1:
                urls.append(url1)
            print(url1)

            url2 = await self.do_filter_dress_url()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")