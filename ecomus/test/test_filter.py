# import pytest

# @pytest.mark.asyncio
# async def test_clearFilter(filter_page):
#     """
#     Verifica que el boton Limpiar Filtros funcione correctamente comparando la cantidad de divs.
#     """
#     divs_collect = await filter_page.doClearFilter()
#     assert len(divs_collect) == len(set(divs_collect)), "Clear filter is not working"

# @pytest.mark.asyncio
# async def test_compare_div(filter_page):
#     """
#     Compara los resultados de aplicar los filtros de 'Hombres' y 'Mujeres' y verifica que sean únicos.
#     """
#     divs_collets = await filter_page.doCompareDivMenWomen()
#     assert len(divs_collets) == len(set(divs_collets)), "The filter is not working "

# @pytest.mark.asyncio
# async def test_outOfStock(filter_page):
#     """
#     Verifica que el filtro de productos fuera de stock funcione correctamente.
#     """
#     total_value = await filter_page.outOfStockFlow()
#     assert total_value > "0", "The cart is not empty, the product still available"

# @pytest.mark.asyncio
# async def test_filterWomen(filter_page):
#     """
#     Verifica que el filtro de 'Mujeres' cambie la URL y los resultados sean únicos.
#     """
#     compare_urls = await filter_page.FilterWomen()
#     assert len(compare_urls) == len(set(compare_urls)), "Filter not working"

# @pytest.mark.asyncio
# async def test_filterMen(filter_page):
#     """
#     Verifica que el filtro de 'Hombres' cambie la URL y los resultados sean únicos.
#     """
#     compare_urls = await filter_page.FilterMen()
#     assert len(compare_urls) == len(set(compare_urls)), "Filter not working"

# @pytest.mark.asyncio
# async def test_filterDenim(filter_page):
#     """
#     Verifica que el filtro de 'Denim' cambie la URL y los resultados sean únicos.
#     """
#     compare_urls = await filter_page.FilterDenim()
#     assert len(compare_urls) == len(set(compare_urls)), "Filter not working"

# @pytest.mark.asyncio
# async def test_filterDress(filter_page):
#     """
#     Verifica que el filtro de 'Dress' cambie la URL y los resultados sean únicos.
#     """
#     compare_urls = await filter_page.FilterDress()
#     assert len(compare_urls) == len(set(compare_urls)), "Filter not working"
