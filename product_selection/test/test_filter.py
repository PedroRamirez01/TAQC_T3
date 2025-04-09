import pytest

#@pytest.mark.asyncio
#async def test_filter_product_men(filter_page):
#    await filter_page.closePopUpHomePage()
#    await filter_page.searchForItem()
#    await filter_page.qckLink()
#    await filter_page.doFilterMen()
#    await filter_page.PopUp()
#    await filter_page.takeScreenshot("filter_product_men.png", fullPage=True)
#
#@pytest.mark.asyncio
#async def test_filter_product_women(filter_page):
#    await filter_page.closePopUpHomePage()
#    await filter_page.searchForItem()
#    await filter_page.qckLink() 
#    await filter_page.doFilterWomen() 
#    await filter_page.PopUp()
#    await filter_page.takeScreenshot("filter_product_women.png", fullPage=True)

@pytest.mark.asyncio
async def test_compare_div(filter_page):
    await filter_page.page.wait_for_timeout(2000)
    await filter_page.closePopUpHomePage()
    await filter_page.searchForItem()
    await filter_page.qckLink()

    await filter_page.doFilterMen()
    await filter_page.PopUp()

    await filter_page.doFilterWomen()
    await filter_page.PopUp()

    result = await filter_page.compare_div()
    assert result, "Los divs deberían ser iguales"