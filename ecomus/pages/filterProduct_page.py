from playwright.async_api import Page
from config.config import Config

class FilterProductPage:
    """
        Modelo de Objeto de Página (POM) para la página de filtrado de productos de Ecomus e-commerce.

        Esta clase implementa el patrón Page Object Model para la funcionalidad de filtrado de productos.
        Proporciona métodos para interactuar con elementos clave de filtrado como:

        - Filtros por categoría (Hombres, Mujeres, Denim, Vestidos)
        - Filtros de disponibilidad de productos
        - Filtros de marca y color
        - Filtros de selección de talla
        - Funcionalidad de limpieza de filtros
        - Interacciones con el carrito de compras

        Características principales:

        - Filtrado de productos por categoría
        - Filtrado de productos por disponibilidad
        - Filtrado de productos por atributos (marca, color, talla)
        - Gestión de filtros (aplicar/limpiar)
        - Funcionalidad de añadir rápido al carrito
        - Manejo de productos fuera de stock

        Flujos principales:

        - doClearFilter: Aplica y limpia filtros, comparando resultados
        - doCompareDivMenWomen: Compara productos entre categorías Hombres y Mujeres
        - outOfStockFlow: Prueba el manejo de productos fuera de stock
        - FilterWomen/FilterMen: Flujos de filtrado por categoría específica
        - FilterDenim/FilterDress: Flujos de filtrado por tipo de producto
        - addCart: Flujo de interacción con el carrito de compras

        Cada flujo incluye manejo de errores y mecanismos de reintento para una operación robusta.
    """
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.filterBttn = self.page.locator(".tf-btn-filter")
        self.filterMen = self.page.locator("li.cate-item:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
        self.filterWomen = self.page.locator("li.cate-item:nth-child(3) > a:nth-child(1) > span:nth-child(1)")
        self.filterDenim = self.page.locator("li.cate-item:nth-child(4) > a:nth-child(1) > span:nth-child(1)")
        self.filterDress = self.page.locator("li.cate-item:nth-child(5) > a:nth-child(1) > span:nth-child(1)")
        self.closePopUp = self.page.locator(".offcanvas-backdrop")
        self.quickAdd = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.addToCart = self.page.locator("div.tf-product-info-buy-button:nth-child(4) > form:nth-child(1) > a:nth-child(1)")
        self.shopCategories = self.page.locator(".tf-sw-collection > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
        self.outOfStockFilter = self.page.locator("#availability > ul:nth-child(1) > li:nth-child(2) > input:nth-child(1)")
        self.producto = self.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")
        self.avaliable = self.page.locator("#availability > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)")
        self.brand = self.page.locator("#brand > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)")
        self.color = self.page.locator("input.bg_brown")
        self.size = self.page.locator("#size > ul:nth-child(1) > li:nth-child(2) > input:nth-child(1)")
        self.clearFilter = self.page.locator("a.tf-btn:nth-child(4)")

    async def navigate(self, url: str) -> None:
        await self.page.goto(url, wait_until="domcontentloaded")

    async def initialURL(self):
        return self.page.url

    async def clear_Filter(self):
        await self.filterBttn.click()
        await self.clearFilter.click()
        await self.closePopUp.click()
        return await self.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()

    async def addCart(self):
        await self.producto.hover()
        await self.producto.wait_for(state="visible")
        await self.quickAdd.click()
        await self.addToCart.click()
        return await self.page.locator(".tf-totals-total-value").inner_text()

    async def outOfStock(self):
        await self.filterBttn.click()
        await self.outOfStockFilter.click()

    async def doFilterMenDiv(self):
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUp.click()
        return await self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()

    async def doFilterWomenDiv(self):
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUp.click()
        return await self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()

    async def doFilterMenURL(self):
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUp.click()
        return self.page.url

    async def doFilterWomenURL(self):
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUp.click()
        return self.page.url

    async def doFilter(self):
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUp.click()
        await self.filterBttn.click()
        await self.avaliable.click()
        await self.brand.click()
        await self.color.click()
        await self.size.click()
        await self.closePopUp.click()
        return await self.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()

    async def doFilterDenimURL(self):
        await self.filterBttn.click()
        for attempy in range(Config.MAX_ATTEMPTS):
            try:
                await self.filterDenim.click()
                await self.closePopUp.click()
                return self.page.url
            except Exception:
                if attempy < Config.MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(Config.DELAY)
        await self.closePopUp.click()

    async def doFilterDressURL(self):
        await self.filterBttn.click()
        for attempy in range(Config.MAX_ATTEMPTS):
            try:
                await self.filterDress.click()
                await self.closePopUp.click()
                return self.page.url
            except Exception:
                if attempy < Config.MAX_ATTEMPTS - 1:
                    await self.page.wait_for_timeout(Config.DELAY)

    async def PopUp(self):
        if await self.closePopUp.count() > 0 and await self.closePopUp.is_visible():
            await self.closePopUp.click()
            await self.page.wait_for_timeout(2000)

    #Flujos que ocupa pytest

    async def outOfStockFlow(self):
        total_value = []
        try:
            await self.outOfStock()
            await self.PopUp()
            total_value = await self.addCart()
            print(f"Total cart value: {total_value}")
            return total_value
        except Exception as e:
            print(f"Error: {e}")

    async def doClearFilter(self):
        divs = []
        try:
            div1 = await self.doFilter()
            if div1:
                divs.append(div1)
                print(div1)
            div2 = await self.clear_Filter()
            if div2:
                divs.append(div2)
                print(div2)
            return divs
        except Exception as e:
            print(f"Error: {e}")

    async def doCompareDivMenWomen(self):
        divs = []	
        try:
            div1 = await self.doFilterMenDiv()
            if div1:
                divs.append(div1)
                print(div1)
            div2 = await self.doFilterWomenDiv()
            if div2:
                divs.append(div2)
                print(div2)
            return divs
        except Exception as e:
            print(f"Error: {e}")

    async def FilterWomen(self):
        urls = []
        try:
            url1 = await self.initialURL()
            if url1:
                urls.append(url1)
            print(url1)
            
            url2 = await self.doFilterWomenURL()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")

    async def FilterMen(self):
        urls = []
        try:
            url1 = await self.initialURL()
            if url1:
                urls.append(url1)
            print(url1)

            url2 = await self.doFilterMenURL()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")

    async def FilterDenim(self):
        urls = []
        try:
            url1 = await self.initialURL()
            if url1:
                urls.append(url1)
            print(url1)

            url2 = await self.doFilterDenimURL()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")

    async def FilterDress(self):
        urls = []
        try:
            url1 = await self.initialURL()
            if url1:
                urls.append(url1)
            print(url1)

            url2 = await self.doFilterDressURL()
            if url2:
                urls.append(url2)
            print(url2)
            return urls
        except Exception as e :
            print(f"Error : {e}")

