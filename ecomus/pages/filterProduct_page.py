from playwright.async_api import Page
from config.config import Config

class FilterProductPage:
    """
    This class implements the Page Object Model pattern for the product filtering functionality.
    It provides methods to interact with key filtering elements such as:

    Category filters (Men, Women, Denim, Dresses)
    Product availability filters
    Brand and color filters
    Size selection filters
    Filter clearing functionality
    Shopping cart interactions

    Main Features:

    Filtering products by category
    Filtering products by availability
    Filtering products by attributes (brand, color, size)
    Filter management (apply/clear)
    Quick add-to-cart functionality
    Handling out-of-stock products

    Main Flows:

    doClearFilter: Applies and clears filters, comparing results
    doCompareDivMenWomen: Compares products between Men and Women categories
    outOfStockFlow: Tests the handling of out-of-stock products
    FilterWomen / FilterMen: Filtering flows for specific categories
    FilterDenim / FilterDress: Filtering flows for specific product types
    addCart: Shopping cart interaction flow

        Each flow includes error handling and retry mechanisms for robust operation.
    """
    def __init__(self, page: Page):
        self.page = page
        self.popUpHome = self.page.locator("span.icon.icon-close.btn-hide-popup")
        self.filterBttn = self.page.locator(".tf-btn-filter")
        self.filterMen = self.page.locator("li.cate-item:nth-child(2) > a:nth-child(1) > span:nth-child(1)")
        self.filterWomen = self.page.locator("li.cate-item:nth-child(3) > a:nth-child(1) > span:nth-child(1)")
        self.filterDenim = self.page.locator("li.cate-item:nth-child(4) > a:nth-child(1) > span:nth-child(1)")
        self.filterDress = self.page.locator("li.cate-item:nth-child(5) > a:nth-child(1) > span:nth-child(1)")
        self.closePopUpFilter = self.page.locator(".offcanvas-backdrop")
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

    async def initial_url(self):
        return self.page.url

    async def clear_Filter(self):
        await self.filterBttn.click()
        await self.clearFilter.click()
        await self.closePopUpFilter.click()
        return await self.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()

    async def add_cart(self):
        await self.producto.hover()
        await self.producto.wait_for(state="visible")
        await self.quickAdd.click()
        await self.addToCart.click()
        return await self.page.locator(".tf-totals-total-value").inner_text()

    async def do_filter_men_div(self): #Refectorizar Return
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUpFilter.click()
        return await self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()

    async def do_filter_women_div(self): #Refectorizar Return
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUpFilter.click()
        return await self.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()

    async def do_filter_men_url(self):
        await self.filterBttn.click()
        await self.filterMen.click()
        await self.closePopUpFilter.click()
        return self.page.url

    async def do_filter_women_url(self):
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUpFilter.click()
        return self.page.url

    async def do_multiplies_filter(self):
        await self.filterBttn.click()
        await self.filterWomen.click()
        await self.closePopUpFilter.click()
        await self.filterBttn.click()
        await self.avaliable.click()
        await self.brand.click()
        await self.color.click()
        await self.size.click()
        await self.closePopUpFilter.click()
        return await self.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()

    async def do_filter_denim_url(self):
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
        await self.filterBttn.click()
        await self.outOfStockFilter.click()

    async def add_cart(self):
        await self.producto.hover()
        await self.producto.wait_for(state="visible")
        await self.quickAdd.click()
        await self.addToCart.click()
        return await self.page.locator(".tf-totals-total-value").inner_text()

    async def pop_up(self):
        if await self.closePopUpFilter.count() > 0 and await self.closePopUpFilter.is_visible():
            await self.closePopUpFilter.click()
            await self.page.wait_for_timeout(2000)

    #Main Flows 

    async def out_of_stock_flow(self):
        total_value = []
        try:
            await self.out_of_stock()
            await self.pop_up()
            total_value = await self.add_cart()
            print(f"Total cart value: {total_value}")
            return total_value
        except Exception as e:
            print(f"Error: {e}")

    async def do_clear_filter(self):
        divs = []
        try:
            div1 = await self.do_multiplies_filter()
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

    async def do_compare_div_men_women(self):
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