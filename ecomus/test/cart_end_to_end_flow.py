import pytest
from playwright.async_api import Page
from playwright.async_api import expect

@pytest.mark.asyncio
@pytest.mark.parametrize("auto_delete_user_e2e", [{
    "email": "luis.rodriguez@gmail.com"
}], indirect=True)
async def test_successful(register_page: Page, login_page: Page, home_page: Page, auto_delete_user_e2e): #, home_page: Page, add_to_cart: Page, checkout_page: Page
    await register_page.navigate()
    await register_page.fill_register_form({
        "first_name": "Luis",
        "last_name": "Rodriguez",
        "email": "luis.rodriguez@gmail.com",
        "password": "Rl1254sZ",
    })
    await register_page.submit()
    
    await expect(register_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/login")
    await login_page.fill_login_form({
        "email": "luis.rodriguez@gmail.com",
        "password": "Rl1254sZ",
    })
    await expect(login_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/my-account")

    await home_page.navigate()
    await home_page.close_pop_up_home()
    await home_page.search_icon_click()
    await home_page.search_input_fill("Paddle")
    await expect(home_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/search?query=Paddle")
