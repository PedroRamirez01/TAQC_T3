import pytest

@pytest.mark.asyncio  # Report bug: la función de buscar por lupa no funciona
async def test_search_product(homeTo_page):
    """
    Verifies that the search by magnifying glass works.
    """
    search_urls = await homeTo_page.search_for_item()
    assert len(search_urls) == len(set(search_urls)), "The URLs are the same, so search doesn't work"

@pytest.mark.asyncio  # Report bug: las nuevas colecciones de home te llevan al mismo link ##Revisar por que no da bug
async def test_descovery_items(homeTo_page):
    """
    Verifies that featured collection links are unique.
    """
    discovery_urls = await homeTo_page.navigate_and_collect_discovery_urls()
    assert len(discovery_urls) == len(set(discovery_urls)), \
        f"Duplicate URLs found. URLs obtained:  {discovery_urls}"

@pytest.mark.asyncio  # Report bug: las categorías de home te llevan a la misma url
async def test_category_items(homeTo_page):
    """
    Verifies that main category links are unique.
    """
    category_urls = await homeTo_page.navigate_and_collect_category_urls()
    assert len(category_urls) == len(set(category_urls)), \
        f"Duplicate URLs found. URLs obtained:  {category_urls}"

@pytest.mark.asyncio
async def test_hover_add_cart(homeTo_page): ##Revisar por que da bug
    """
    Verifies that the Quick Add popup displays correctly when hovering and clicking on the first product, and adds it to cart.
    """
    was_popup_visible = await homeTo_page.hover_product_and_quick_add()
    assert was_popup_visible, "Quick Add popup content did not become visible after hover and click."

@pytest.mark.asyncio
async def test_hover_add_fav(homeTo_page): ##Revisar por que da bug
    """
    Verifies that the Quick Fav popup displays correctly when hovering and clicking on the first product.
    """
    was_popup_visible = await homeTo_page.hover_product_and_add_fav()
    assert was_popup_visible, "Quick Fav popup content did not become visible after hover and click."

@pytest.mark.asyncio
async def test_hover_add_compare(homeTo_page):
    """
    Verifies that the Quick Compare popup displays correctly when hovering and clicking on the first product.
    """
    was_popup_visible = await homeTo_page.hover_product_and_add_compare()
    assert was_popup_visible, "Quick Add to Compare is not visible"

@pytest.mark.asyncio
async def test_hover_view(homeTo_page):
    """
    Verifies that the Quick View popup displays correctly when hovering and clicking on the first product.
    """
    was_popup_visible = await homeTo_page.hover_product_and_view()
    assert was_popup_visible, "Quick View is not visible"