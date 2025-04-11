import pytest

@pytest.mark.asyncio
async def test_compare_div(filter_page):
    await filter_page.page.wait_for_timeout(2000)
    await filter_page.closePopUpHomePage()
    await filter_page.shopByCategories()
    await filter_page.doFilterMen()
    await filter_page.PopUp()
    await filter_page.doFilterWomen()
    await filter_page.PopUp()
    result = await filter_page.compare_div()
    print(f"Result of comparison: {result}")
    assert result, "The divs are not the same"