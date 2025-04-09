import pytest

@pytest.mark.asyncio
async def test_search_product(search_page):
    await search_page.search_for_item("Paddle", max_attempts=2, delay=1000)
    assert "/item-paddle" in search_page.page.url, "Search URL is not correct"