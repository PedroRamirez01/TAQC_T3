import pytest
from playwright.async_api import expect , Page
from pages.home_page import HomeToPage

@pytest.mark.asyncio
async def test_search_product(page:Page):
    homeTo_page = HomeToPage(page)
    """
    Verifies that the search by magnifying glass works.
    """
    search_result = await homeTo_page.search_for_item()
    await expect(homeTo_page.searchInput).to_have_value("Paddle") #To verify if the search input is filled with the correct value

    final_url = search_result[0]

    await expect(homeTo_page.page).not_to_have_url(final_url,timeout=3000)

@pytest.mark.asyncio
async def test_hover_add_cart(page:Page):
    homeTo_page = HomeToPage(page)
    """
    Verifies that the Quick Add popup displays correctly when hovering and clicking on the first product.
    """
    await homeTo_page.close_pop_up_home()
    await homeTo_page.franklinSiganture.scroll_into_view_if_needed()
    await homeTo_page.franklinSiganture.hover()
    await expect(homeTo_page.quickAdd).to_be_visible(timeout=2000)
    await homeTo_page.quickAdd.click()
    await expect(homeTo_page.quickAddPopupContent).to_be_visible(timeout=3000)

@pytest.mark.asyncio
async def test_hover_add_fav(page:Page):
    homeTo_page = HomeToPage(page)
    """
    Verifies that the Quick Fav popup displays correctly when hovering and clicking on the first product.
    """
    await homeTo_page.close_pop_up_home()
    await homeTo_page.franklinSiganture.scroll_into_view_if_needed()
    await homeTo_page.franklinSiganture.hover()
    await expect(homeTo_page.quickAddFav).to_be_visible(timeout=2000)
    await homeTo_page.quickAddFav.click()
    await expect(homeTo_page.quickAddFavPopupContent).to_be_visible(timeout=3000)

@pytest.mark.asyncio
async def test_hover_add_compare(page:Page):
    homeTo_page = HomeToPage(page)
    """
    Verifies that the Quick Compare popup displays correctly when hovering and clicking on the first product.
    """
    await homeTo_page.close_pop_up_home()
    await homeTo_page.franklinSiganture.scroll_into_view_if_needed()
    await homeTo_page.franklinSiganture.hover()
    await expect(homeTo_page.quickAddCompare).to_be_visible(timeout=2000)
    await homeTo_page.quickAddCompare.click()
    await homeTo_page.closerCompare.click()
    await expect(homeTo_page.quickAddComparePopupContent).to_be_visible(timeout=3000)


@pytest.mark.asyncio
async def test_hover_view(page:Page):
    homeTo_page = HomeToPage(page)
    """
    Verifies that the Quick View popup displays correctly when hovering and clicking on the first product.
    """
    await homeTo_page.close_pop_up_home()
    await homeTo_page.franklinSiganture.scroll_into_view_if_needed()
    await homeTo_page.franklinSiganture.hover()
    await expect(homeTo_page.quickView).to_be_visible(timeout=2000)
    await homeTo_page.quickView.click()
    await expect(homeTo_page.quickViewPopupContent).to_be_visible(timeout=3000)