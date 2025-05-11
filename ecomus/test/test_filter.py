import pytest
from playwright.async_api import expect


#@pytest.mark.asyncio
#async def test_outOfStock(filter_page):
#    """
#    Verifies that the out of stock products filter works correctly.
#    """
#    cart_total_locator = await filter_page.out_of_stock_flow()
#    await expect(cart_total_locator).to_have_text("0")

@pytest.mark.asyncio
async def test_clearFilter(filter_page):
    """
    Verifies that the Clear Filters button works correctly.
    """
    clearFilterButton = await filter_page.do_clear_filter()
    await expect(clearFilterButton).to_be_enabled()
    await clearFilterButton.click()

#@pytest.mark.asyncio
#async def test_compare_div(filter_page):
#    """
#    Compares the results of applying 'Men' and 'Women' filters and verifies they are unique.
#    """
#    divs_collets = await filter_page.do_compare_div_men_women()
#    assert len(divs_collets) == len(set(divs_collets)), "The filter is not working "
#
#@pytest.mark.asyncio
#async def test_filterWomen(filter_page):
#    """
#    Verifies that the 'Women' filter changes the URL and results are unique.
#    """
#    compare_urls = await filter_page.filter_women()
#    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"
#
#@pytest.mark.asyncio
#async def test_filterMen(filter_page):
#    """
#    Verifies that the 'Men' filter changes the URL and results are unique.
#    """
#    compare_urls = await filter_page.filter_men()
#    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"
#
#@pytest.mark.asyncio
#async def test_filterDenim(filter_page):
#    """
#    Verifies that the 'Denim' filter changes the URL and results are unique.
#    """
#    compare_urls = await filter_page.filter_denim()
#    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"
#
#@pytest.mark.asyncio
#async def test_filterDress(filter_page):
#    """
#    Verifies that the 'Dress' filter changes the URL and results are unique.
#    """
#    compare_urls = await filter_page.filter_dress()
#    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"
