import pytest

@pytest.mark.asyncio
async def test_clearFilter(filter_page): #Clear filter good
    divs_collect = await filter_page.doClearFilter()
    assert len(divs_collect) == len(set(divs_collect)) , "Clear filter is not working "

@pytest.mark.asyncio
async def test_compare_div(filter_page): 
    divs_collets = await filter_page.doCompareDivMenWomen() #The filter works pero no cambian las divs
    assert len(divs_collets) == len(set(divs_collets)), "The filter is not working as expected"

@pytest.mark.asyncio
async def test_outOfStock(filter_page):  #Report bug el filtro out of stock no sirve, ya que puedo agregar productos al carro
    total_value = await filter_page.outOfStockFlow()
    assert total_value > "0", "The cart is not empty, the product still available"

@pytest.mark.asyncio          #Report Bug URL Cambia pero los productos no cambian
async def test_filterWomen(filter_page):
    compare_urls = await filter_page.FilterWomen()
    assert len(compare_urls) == len(set(compare_urls)) , "Filter not working"

@pytest.mark.asyncio            #Report Bug URL Cambia pero los productos no cambian
async def test_filterMen(filter_page):
    compare_urls = await filter_page.FilterMen()
    assert len(compare_urls) == len(set(compare_urls)) , "Filter not working"

@pytest.mark.asyncio
async def test_filterDenim(filter_page): #Report bug este filtro no hace nada
    compare_urls = await filter_page.FilterDenim()
    assert len(compare_urls) == len(set(compare_urls)) , "Filter not working"

@pytest.mark.asyncio
async def test_filterDress(filter_page): #Report bug este filtro no hace nada
    compare_urls = await filter_page.FilterDress()
    assert len(compare_urls) == len(set(compare_urls)) , "Filter not working"
