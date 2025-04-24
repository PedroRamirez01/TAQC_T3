from playwright.async_api import Page
from config.config import Config

class HomeToPage:
    """
        Modelo de Objeto de Página (POM) para la página principal de Ecomus e-commerce.

        Esta clase implementa el patrón Page Object Model para la página principal del sitio web Ecomus.
        Proporciona métodos para interactuar con elementos clave como:

        - Botones de navegación y categorías
        - Funcionalidad de búsqueda
        - Acciones rápidas (Agregar al carrito, favoritos, comparar)
        - Características de descubrimiento de productos
        - Gestión de ventanas emergentes

        Características principales:

        - Navegación por categorías (Ropa, Paddles, Accesorios, Hombres)
        - Búsqueda y filtrado de productos
        - Funcionalidad de vista rápida y agregar al carrito
        - Funciones de lista de deseos y comparación de productos
        - Secciones de descubrimiento (Nuevos Artículos, Super Store, Serie SLK, Motion Pro)

        Flujos principales:

        - search_for_item: Realiza búsqueda de productos usando el icono y campo de búsqueda
        - navigate_and_collect_discovery_urls: Navega por las secciones destacadas y recolecta URLs
        - navigate_and_collect_category_urls: Navega por las categorías principales y recolecta URLs
        - hover_product_and_quick_add: Agrega producto al carrito mediante acción rápida
        - hover_product_and_add_fav: Agrega producto a favoritos mediante acción rápida
        - hover_product_and_add_compare: Agrega producto a comparación mediante acción rápida
        - hover_product_and_view: Muestra vista rápida del producto
    """

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
    
    async def closePopUpHome(self):
        await self.page.wait_for_timeout(2000)
        await self.popUpHome.click()

    async def closerQuickView(self):
        await self.page.wait_for_timeout(2000)
        await self.closerQuick.click()
    
    async def click_clothingButton(self):
        await self.clothingButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url
    
    async def click_paddlesButton(self):
        await self.paddlesButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url
    
    async def click_accesoriesButton(self):
        await self.accesoriesButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url
    
    async def click_menButton(self):
        await self.menButton.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_newItems(self):
        await self.newItems.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_superStore(self):
        await self.superStore.scroll_into_view_if_needed()
        await self.superStore.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_slkSeries(self):
        await self.slkSeries.scroll_into_view_if_needed()
        await self.slkSeries.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_motionPro(self):
        await self.motionPro.scroll_into_view_if_needed()
        await self.motionPro.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def click_ecomus(self):
        await self.ecomus.click()
        await self.page.wait_for_timeout(1000)

    async def searchIconClick(self):
        await self.searchIcon.click()
        await self.page.wait_for_timeout(1000)
        return self.page.url

    async def searchInputFill(self, item: str = "Paddle"):
        await self.searchInput.fill(item)
        await self.page.wait_for_timeout(1000)
        return self.page.url

    # Flujos de los test

    async def search_for_item(self):
        urls = []
        for attempt in range(Config.MAX_ATTEMPTS):
            try:
                url1 = await self.searchIconClick()
                if url1: urls.append(url1)
                await self.page.wait_for_timeout(1000)

                url2 = await self.searchInputFill()
                if url2: urls.append(url2)

                return urls
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < Config.MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(Config.DELAY)
    
    async def navigate_and_collect_discovery_urls(self):
        collected_urls = []
        try:
            await self.closePopUpHome()

            url1 = await self.click_newItems()
            if url1: collected_urls.append(url1)

            await self.click_ecomus()
            await self.closePopUpHome()

            url2 = await self.click_superStore()
            if url2: collected_urls.append(url2)

            await self.click_ecomus()
            await self.closePopUpHome()

            url3 = await self.click_slkSeries()
            if url3: collected_urls.append(url3)

            await self.click_ecomus()
            await self.closePopUpHome()

            url4 = await self.click_motionPro()
            if url4: collected_urls.append(url4)

        except Exception as e:
            print(f"Error durante la secuencia de navegación: {e}")
        return collected_urls

    async def navigate_and_collect_category_urls(self):
        collected_urls = []
        try:
            await self.closePopUpHome()
            url1 = await self.click_clothingButton()
            if url1: collected_urls.append(url1)

            await self.click_ecomus()
            await self.closePopUpHome()

            url2 = await self.click_paddlesButton()
            if url2: collected_urls.append(url2)

            await self.click_ecomus()
            await self.closePopUpHome()

            url3 = await self.click_accesoriesButton()
            if url3: collected_urls.append(url3)

            await self.click_ecomus()
            await self.closePopUpHome()
            await self.nextButton.click()

            url4 = await self.click_menButton()
            if url4: collected_urls.append(url4)
        except Exception as e:
            print(f"Error al recolectar urls: {e}")
        return collected_urls

    async def hover_product_and_quick_add(self):
        try:
            await self.closePopUpHome()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickAdd.wait_for(state="visible", timeout=2000)
            await self.quickAdd.click()
            await self.quickAddPopupContent.wait_for(state="visible", timeout=2000)
            print("Contenido del Quick Add visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y añadir al carrito: {e}")
            return False
    
    async def hover_product_and_add_fav(self):
        try:
            await self.closePopUpHome()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickAddFav.wait_for(state="visible", timeout=2000)
            await self.quickAddFav.click()
            await self.quickAddFavPopupContent.wait_for(state="visible", timeout=2000)
            print("Contenido del Quick Fav visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y añadir a favoritos: {e}")
            return False
    
    async def hover_product_and_add_compare(self):
        try:
            await self.closePopUpHome()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickAddCompare.wait_for(state="visible", timeout=2000)
            await self.quickAddCompare.click()
            await self.closerCompare.click()
            await self.quickAddComparePopupContent.wait_for(state="visible", timeout=2000)
            print("Contenido del Quick Compare visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y añadir a comparar: {e}")
            return False
    
    async def hover_product_and_view(self):
        try:
            await self.closePopUpHome()
            await self.franklinSiganture.scroll_into_view_if_needed()
            await self.franklinSiganture.hover()
            await self.quickView.wait_for(state="visible", timeout=2000)
            await self.quickView.click()
            await self.quickViewPopupContent.wait_for(state="visible", timeout=2000)
            print("Contenido del Quick View visible")
            return True
        except Exception as e:
            print(f"Error al intentar hacer hover y ver el producto: {e}")
            return False