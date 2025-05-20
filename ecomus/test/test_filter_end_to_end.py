import pytest
from playwright.async_api import Page , expect

@pytest.mark.asyncio
@pytest.mark.parametrize("auto_delete_user_e2e", [{
    "email": "luis.rodriguez@gmail.com"
}], indirect=True)
async def test_successful_filter(register_page: Page, login_page: Page, homeTo_page: Page, filter_page: Page,checkout_page: Page, auto_delete_user_e2e): #, home_page: Page, add_to_cart: Page, checkout_page: Page
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
    await filter_page.move_price_slider(1)
    await filter_page.move_price_slider(7) #Valor 16-20 Slicer
    #await filter_page.pop_up()
    await filter_page.order_by()
    await expect(filter_page.page.locator("div.card-product:nth-child(1) > div:nth-child(2) > span:nth-child(2)")).to_have_text("$14.95")
    
    #await filter_page.out_of_stock() #Bug 1 es posible añadir al carrito un producto que no tiene stock

    color_element = await filter_page.click_color()
    await expect(color_element).to_have_text("Brown")

    await filter_page.click_Brand()

    size_element = await filter_page.size_XL()
    await expect(size_element).to_have_text("XL")

    await filter_page.add_cart()

    await checkout_page.clickTermsAndConditionsCheckbox()
    await checkout_page.clickProceedToCheckoutButton()
    await checkout_page.fillCheckoutForm({
        "FIRST_NAME": "Luis",
        "LAST_NAME": "González",
        "COUNTRY": "United States",
        "CITY": "Springfield",
        "ADDRESS": "Calle siempre viva 123",
        "PHONE_NUMBER": "123456789",
        "EMAIL": "pedritogonzalez123@gmail.com",
        "DISCOUNT_CODE": "123",
        "CARD_NUMBER": "4242424242424242",
        "CARD_EXPIRATION": "12/25",
        "CARD_CVV": "123"
    })

    await checkout_page.clickAgreeCheckbox()
    await checkout_page.clickPlaceOrderButton()

    await expect(checkout_page.successMessage).to_contain_text("Order saved successfully! Your order ID is:")