import pytest

@pytest.mark.asyncio  # Report bug: la función de buscar por lupa no funciona
async def test_searchProduct(homeTo_page):
    """
    Verifica que la búsqueda por lupa funcione.
    """
    search_urls = await homeTo_page.search_for_item()
    assert len(search_urls) == len(set(search_urls)), "The URLs are the same, so search doesn't work"

@pytest.mark.asyncio  # Report bug: las nuevas colecciones de home te llevan al mismo link
async def test_descoveryItems(homeTo_page):
    """
    Verifica que los enlaces de las colecciones destacadas sean únicos.
    """
    discovery_urls = await homeTo_page.navigate_and_collect_discovery_urls()
    assert len(discovery_urls) == len(set(discovery_urls)), \
        f"Se encontraron URLs duplicadas. URLs obtenidas:  {discovery_urls}"

@pytest.mark.asyncio  # Report bug: las categorías de home te llevan a la misma url
async def test_categoryItems(homeTo_page):
    """
    Verifica que los enlaces de las categorías principales sean únicos.
    """
    category_urls = await homeTo_page.navigate_and_collect_category_urls()
    assert len(category_urls) == len(set(category_urls)), \
        f"Se encontraron URLs duplicadas. URLs obtenidas:  {category_urls}"

@pytest.mark.asyncio
async def test_hoverAddCart(homeTo_page):
    """
    Verifica que el popup de Quick Add se muestre correctamente al hacer hover y clic en el primer producto, ademas de agregarlo al carrito.
    """
    was_popup_visible = await homeTo_page.hover_product_and_quick_add()
    assert was_popup_visible, "El contenido del popup de Quick Add no se hizo visible después de hacer hover y clic."

@pytest.mark.asyncio
async def test_hoverAddFav(homeTo_page):
    """
    Verifica que el popup de Quick Fav se muestre correctamente al hacer hover y clic en el primer producto.
    """
    was_popup_visible = await homeTo_page.hover_product_and_add_fav()
    assert was_popup_visible, "El contenido del popup de Quick Fav no se hizo visible después de hacer hover y clic."

@pytest.mark.asyncio
async def test_hoverAddCompare(homeTo_page):
    """
    Verifica que el popup de Quick Compare se muestre correctamente al hacer hover y clic en el primer producto.
    """
    was_popup_visible = await homeTo_page.hover_product_and_add_compare()
    assert was_popup_visible, "Quick Add to Compare is not visible"

@pytest.mark.asyncio
async def test_hoverView(homeTo_page):
    """
    Verifica que el popup de Quick View se muestre correctamente al hacer hover y clic en el primer producto.
    """
    was_popup_visible = await homeTo_page.hover_product_and_view()
    assert was_popup_visible, "Quick View is not visible"