import pytest

@pytest.mark.asyncio
async def test_search_product(search_page):
    initial_url = search_page.page.url
    print(f"Initial URL: {initial_url}")
    await search_page.page.wait_for_timeout(2000)
    await search_page.closePopUpHomePage()
    await search_page.searchIcons()
    await search_page.search_for_item("Paddle", max_attempts=2, delay=2000)
    current_url = search_page.page.url
    assert current_url == initial_url
    print(f"Final URL: {current_url}")
    