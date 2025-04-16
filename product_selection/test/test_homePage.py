import pytest

@pytest.mark.asyncio
async def test_searchProduct(homeTo_page):
    initial_url = homeTo_page.page.url
    await homeTo_page.closePopUpHome()
    await homeTo_page.search_for_item("Paddle")
    current_url = homeTo_page.page.url
    assert current_url != initial_url, "The URLS are the same, so search doesn't work" #Opinion assertion de este test...

@pytest.mark.asyncio         #Opinion de este test...
async def test_homeCategories(homeTo_page):
    await homeTo_page.closePopUpHome()
    await homeTo_page.click_newItems()
    url1 = homeTo_page.page.url
    await homeTo_page.click_ecomus()
    await homeTo_page.closePopUpHome()
    await homeTo_page.click_superStore()
    url2 = homeTo_page.page.url
    await homeTo_page.click_ecomus()
    await homeTo_page.closePopUpHome()
    await homeTo_page.click_slkSeries()
    url3 = homeTo_page.page.url
    await homeTo_page.click_ecomus()
    await homeTo_page.closePopUpHome()
    await homeTo_page.click_motionPro()
    url4 = homeTo_page.page.url
    await homeTo_page.click_ecomus()
    assert url1 != url2 != url3 != url4 , "URLs are the same"

@pytest.mark.asyncio
async def test_hoverAddCart(homeTo_page):
    await homeTo_page.productHoverAddCart()
    assert await homeTo_page.page.locator ("#quick_add > div:nth-child(1) > div:nth-child(1)").is_visible() == True, "Quick Add to Cart is not visible"

@pytest.mark.asyncio
async def test_hoverAddFav(homeTo_page):
    await homeTo_page.productHoverAddFav()
    assert await homeTo_page.page.locator("div.card-product:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > span:nth-child(2)").is_visible() == True, "Quick Add to Favorites is not visible"

@pytest.mark.asyncio
async def test_hoverAddCompare(homeTo_page):
    await homeTo_page.productHoverAddCompare()
    assert await homeTo_page.page.locator("#compare > div:nth-child(1) > div:nth-child(2)").is_visible() == True, "Quick Add to Compare is not visible"

@pytest.mark.asyncio
async def test_hoverView(homeTo_page):
    await homeTo_page.productHoverView()
    assert await homeTo_page.page.locator("div.tf-product-info-list:nth-child(1)").is_visible() == True, "Quick View is not visible"