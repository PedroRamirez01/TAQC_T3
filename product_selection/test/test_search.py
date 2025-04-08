import pytest

@pytest.mark.asyncio
async def test_search_product(search_page):
    await search_page.search_for_item("Paddle")
    assert await search_page.get_search_results_count() > 0, "No search results found"
    assert await search_page.get_search_results_text() == "Paddle", "Search results do not match the expected item"