from playwright.async_api import Page
from config.config import Config

class FilterProductPage:
    """
    Page Object Model para la página de filtrado de productos.
    Permite aplicar, limpiar y comparar filtros, así como interactuar con productos y el carrito.
    """
    def __init__(self, page: Page):
        """
        Inicializa los localizadores de la página de filtrado de productos.
        :param page: Instancia de Playwright Page.
        """
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

    async def initialURL(self):
        """
        Retorna la URL actual de la página.
        """
        return self.page.url

    async def navigate(self, url: str) -> None:
        """
        Navega a la URL especificada.
        :param url: URL de destino.
        """
        await self.page.goto(url, wait_until="domcontentloaded")

    async def doFilter(self):
        """
        Aplica varios filtros y retorna el texto del contenedor de resultados.
        :return: Texto del div de resultados.
        """
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

    async def clear_Filter(self):
        """
        Limpia los filtros aplicados y retorna el texto del contenedor de resultados.
        :return: Texto del div de resultados.
        """
        await self.filterBttn.click()
        await self.clearFilter.click()
        await self.closePopUp.click()
        return await self.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()

    async def addCart(self):
        """
        Añade el primer producto visible al carrito y retorna el valor total del carrito.
        :return: Valor total del carrito.
        """
        await self.producto.hover()
        await self.producto.wait_for(state="visible")
        await self.quickAdd.click()
        await self.addToCart.click()
        return await self.page.locator(".tf-totals-total-value").inner_text()

    async def outOfStock(self):
        """
        Aplica el filtro de productos fuera de stock.
        """
        await self.filterBttn.click()
        await self.outOfStockFilter.click()

    async def doFilterMenDiv(self):
        """
        Aplica el filtro de 'Hombres' y retorna el texto del primer producto.
        :return: Texto del div del primer producto filtrado por hombres.
        """
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUp.click()
        return await self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()

    async def doFilterWomenDiv(self):
        """
        Aplica el filtro de 'Mujeres' y retorna el texto del primer producto.
        :return: Texto del div del primer producto filtrado por mujeres.
        """
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUp.click()
        return await self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()

    async def doFilterMenURL(self):
        """
        Aplica el filtro de 'Hombres' y retorna la URL actual.
        :return: URL después de aplicar el filtro.
        """
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUp.click()
        return self.page.url

    async def doFilterWomenURL(self):
        """
        Aplica el filtro de 'Mujeres' y retorna la URL actual.
        :return: URL después de aplicar el filtro.
        """
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUp.click()
        return self.page.url

    async def doFilterDenimURL(self):
        """
        Aplica el filtro de 'Denim' con reintentos y retorna la URL actual.
        :return: URL después de aplicar el filtro.
        """
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
        return self.page.url

    async def doFilterDressURL(self):
        """
        Aplica el filtro de 'Dress' con reintentos y retorna la URL actual.
        :return: URL después de aplicar el filtro.
        """
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
        """
        Cierra el pop-up si está visible y espera 2 segundos.
        """
        if await self.closePopUp.count() > 0 and await self.closePopUp.is_visible():
            await self.closePopUp.click()
            await self.page.wait_for_timeout(2000)

    #Flujos que ocupa pytest

    async def doClearFilter(self):
        """
        Aplica un filtro, luego lo limpia y retorna una lista con los textos de los divs antes y después de limpiar.
        :return: Lista con los textos de los divs antes y después de limpiar el filtro.
        """
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
        """
        Aplica los filtros de 'Hombres' y 'Mujeres', retorna una lista con los textos de los divs de ambos.
        :return: Lista con los textos de los divs filtrados por hombres y mujeres.
        """
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

    async def outOfStockFlow(self):
        """
        Aplica el filtro de fuera de stock, intenta agregar al carrito y retorna el valor total del carrito.
        :return: Valor total del carrito después del intento.
        """
        total_value = []
        try:
            await self.outOfStock()
            await self.PopUp()
            total_value = await self.addCart()
            print(f"Total cart value: {total_value}")
            return total_value
        except Exception as e:
            print(f"Error: {e}")

    async def FilterWomen(self):
        """
        Obtiene la URL inicial y la URL después de aplicar el filtro de 'Mujeres'.
        :return: Lista con la URL inicial y la URL después del filtro.
        """
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
        """
        Obtiene la URL inicial y la URL después de aplicar el filtro de 'Hombres'.
        :return: Lista con la URL inicial y la URL después del filtro.
        """
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
        """
        Obtiene la URL inicial y la URL después de aplicar el filtro de 'Denim'.
        :return: Lista con la URL inicial y la URL después del filtro.
        """
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
        """
        Obtiene la URL inicial y la URL después de aplicar el filtro de 'Dress'.
        :return: Lista con la URL inicial y la URL después del filtro.
        """
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

