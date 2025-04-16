import pytest

@pytest.mark.asyncio
async def test_clearFilter(filter_page):
    await filter_page.clearFilterStep1()
    products_before = await filter_page.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()
    await filter_page.clearFilterStep2()
    products_after = await filter_page.page.locator(".wrapper-control-shop > div:nth-child(2)").inner_text()
    assert products_after != products_before , "Clear filter is not working "

@pytest.mark.asyncio
async def test_compare_div(filter_page):
    div1 = await filter_page.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()
    await filter_page.doFilterMen()
    div2 = await filter_page.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()
    await filter_page.PopUp()
    await filter_page.doFilterWomen()
    div3 = await filter_page.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > a:nth-child(1)").inner_text()
    await filter_page.PopUp()
    assert div1 != div2 and div1 != div3 and div2 != div3 , "The Divs are the same"

@pytest.mark.asyncio
async def test_outOfStock(filter_page):
    await filter_page.outOfStockFlow()
    result = await filter_page.totalCart_value()
    #print(f"Total cart value: {result}")
    assert result > "0", "The cart is not empty, the product still available"

@pytest.mark.asyncio          #Report Bug URL Cambia pero los productos no cambian
async def test_filterMen(filter_page):
    initial_url = filter_page.page.url
    await filter_page.doFilterMen()
    current_url = filter_page.page.url
    assert current_url != initial_url, "Filter not working as expected"

@pytest.mark.asyncio            #Report Bug URL Cambia pero los productos no cambian
async def test_filterWomen(filter_page):
    initial_url = filter_page.page.url
    await filter_page.doFilterWomen()
    current_url = filter_page.page.url
    assert current_url != initial_url, "Filter not working as expected"

@pytest.mark.asyncio
async def test_filterDenim(filter_page): #DUDA! click
    initial_url = filter_page.page.url
    await filter_page.filterNotWorkingDenim()
    current_url = filter_page.page.url
    assert current_url != initial_url, "Filter not working as expected"

@pytest.mark.asyncio
async def test_filterDress(filter_page):
    initial_url = filter_page.page.url
    await filter_page.filterNotWorkingDress()
    current_url = filter_page.page.url
    assert current_url != initial_url, "Filter not working as expected"
