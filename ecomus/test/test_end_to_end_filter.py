import pytest
import time
from playwright.async_api import Page , expect

@pytest.mark.asyncio
@pytest.mark.parametrize("auto_delete_user_e2e", [{
    "email": "luis.rodriguez@gmail.com"
}], indirect=True)
async def test_successful(register_page: Page, login_page: Page, homeTo_page: Page, filter_page: Page, auto_delete_user_e2e): #, home_page: Page, add_to_cart: Page, checkout_page: Page
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

    await homeTo_page.click_ecomus()
    await homeTo_page.close_pop_up_home()
    await homeTo_page.search_icon_click()
    await homeTo_page.fashion_search()
    await expect(homeTo_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/shop-default")

    await filter_page.do_filter_men()
    await expect(filter_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/shop-men")
    await filter_page.do_filter_women()
    await expect(filter_page.page).to_have_url("https://automation-portal-bootcamp.vercel.app/shop-women")
    await filter_page.filterBttn.click()
    await filter_page.move_price_slider(-50)
    await filter_page.move_price_slider(50) #Valor 13 Slicer
    
    
    
    #await filter_page.out_of_stock()
    #await filter_page.productThree.click()
    time.sleep(3)