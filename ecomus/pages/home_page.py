from playwright.async_api import Page
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
        self.quickAddPopupContent = page.locator("#quick_add > div:nth-child(1) > div:nth-child(1)")
        self.quickAddFavPopupContent = page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > span:nth-child(2)")
        self.quickAddComparePopupContent = page.locator("#compare > div:nth-child(1) > div:nth-child(2)")
        self.quickViewPopupContent = page.locator("div.tf-product-info-list:nth-child(1)")
        self.clothingButton = page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.paddlesButton = page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.accesoriesButton = page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.nextButton = page.locator("div.nav-prev-slider:nth-child(2)")
        self.menButton = page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")

    async def navigate(self, url: str) -> None:
        assert await self.page.goto(url, wait_until="domcontentloaded")
    
    async def close_pop_up_home(self):
        await self.popUpHome.wait_for(state="visible")
        await self.page.wait_for_load_state("networkidle")
        await self.popUpHome.click()

    async def closer_quick_view(self):
        await self.page.wait_for_timeout(2000)
        await self.closerQuick.click()
    
    async def click_clothing_button(self):
        await self.clothingButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url
    
    async def click_paddles_button(self):
        await self.paddlesButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url
    
    async def click_accesories_button(self):
        await self.accesoriesButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url
    
    async def click_men_button(self):
        await self.menButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_new_items(self):
        await self.newItems.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_super_store(self):
        await self.superStore.scroll_into_view_if_needed()
        await self.superStore.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_slk_series(self):
        await self.slkSeries.scroll_into_view_if_needed()
        await self.slkSeries.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_motion_pro(self):
        await self.motionPro.scroll_into_view_if_needed()
        await self.motionPro.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

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
    
    async def navigate_and_collect_discovery_urls(self):
        collected_urls = []
        try:
            await self.close_pop_up_home()

            url1 = await self.click_new_items()
            if url1: collected_urls.append(url1)

            await self.click_ecomus()
            await self.close_pop_up_home()

            url2 = await self.click_super_store()
            if url2: collected_urls.append(url2)

            await self.click_ecomus()
            await self.close_pop_up_home()

            url3 = await self.click_slk_series()
            if url3: collected_urls.append(url3)

            await self.click_ecomus()
            await self.close_pop_up_home()

            url4 = await self.click_motion_pro()
            if url4: collected_urls.append(url4)

        except Exception as e:
            print(f"Error durante la secuencia de navegación: {e}")
        return collected_urls

    async def navigate_and_collect_category_urls(self):
        collected_urls = []
        try:
            await self.close_pop_up_home()
            url1 = await self.click_clothing_button()
            if url1: collected_urls.append(url1)

            await self.click_ecomus()
            await self.close_pop_up_home()

            url2 = await self.click_paddles_button()
            if url2: collected_urls.append(url2)

            await self.click_ecomus()
            await self.close_pop_up_home()

            url3 = await self.click_accesories_button()
            if url3: collected_urls.append(url3)

            await self.click_ecomus()
            await self.close_pop_up_home()
            await self.nextButton.click()

            url4 = await self.click_men_button()
            if url4: collected_urls.append(url4)
        except Exception as e:
            print(f"Error al recolectar urls: {e}")
        return collected_urls

    async def hover_product_and_quick_add(self):
        try:
            await self.close_pop_up_home()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickAdd.wait_for(state="visible", timeout=2000)
            await self.quickAdd.click()
            await self.quickAddPopupContent.wait_for(state="visible", timeout=3000)
            print("Contenido del Quick Add visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y añadir al carrito: {e}")
            return False
    
    async def hover_product_and_add_fav(self):
        try:
            await self.close_pop_up_home()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickAddFav.wait_for(state="visible", timeout=2000)
            await self.quickAddFav.click()
            await self.quickAddFavPopupContent.wait_for(state="visible", timeout=3000)
            print("Contenido del Quick Fav visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y añadir a favoritos: {e}")
            return False
    
    async def hover_product_and_add_compare(self):
        try:
            await self.close_pop_up_home()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickAddCompare.wait_for(state="visible", timeout=2000)
            await self.quickAddCompare.click()
            await self.closerCompare.click()
            await self.quickAddComparePopupContent.wait_for(state="visible", timeout=3000)
            print("Contenido del Quick Compare visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y añadir a comparar: {e}")
            return False
    
    async def hover_product_and_view(self):
        try:
            await self.close_pop_up_home()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickView.wait_for(state="visible", timeout=2000)
            await self.quickView.click()
            await self.quickViewPopupContent.wait_for(state="visible", timeout=3000)
            print("Contenido del Quick View visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y ver el producto: {e}")
            return False