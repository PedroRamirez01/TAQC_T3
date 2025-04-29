import pytest

@pytest.mark.asyncio
async def test_clearFilter(filter_page):
    """
    Verifies that the Clear Filters button works correctly by comparing the number of divs.
    """
    divs_collect = await filter_page.do_clear_filter()
    assert len(divs_collect) == len(set(divs_collect)), "Clear filter is not working"

@pytest.mark.asyncio
async def test_compare_div(filter_page):
    """
    Compares the results of applying 'Men' and 'Women' filters and verifies they are unique.
    """
    divs_collets = await filter_page.do_compare_div_men_women()
    assert len(divs_collets) == len(set(divs_collets)), "The filter is not working "

@pytest.mark.asyncio
async def test_outOfStock(filter_page):
    """
    Verifies that the out of stock products filter works correctly.
    """
    total_value = await filter_page.out_of_stock_flow()
    assert total_value > "0", "The cart is not empty, the product still available"

@pytest.mark.asyncio
async def test_filterWomen(filter_page):
    """
    Verifies that the 'Women' filter changes the URL and results are unique.
    """
    compare_urls = await filter_page.filter_women()
    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"

@pytest.mark.asyncio
async def test_filterMen(filter_page):
    """
    Verifies that the 'Men' filter changes the URL and results are unique.
    """
    compare_urls = await filter_page.filter_men()
    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"

@pytest.mark.asyncio
async def test_filterDenim(filter_page):
    """
    Verifies that the 'Denim' filter changes the URL and results are unique.
    """
    compare_urls = await filter_page.filter_denim()
    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"

@pytest.mark.asyncio
async def test_filterDress(filter_page):
    """
    Verifies that the 'Dress' filter changes the URL and results are unique.
    """
    compare_urls = await filter_page.filter_dress()
    assert len(compare_urls) == len(set(compare_urls)), "Filter not working"
