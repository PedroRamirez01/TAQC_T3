from playwright.async_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.termsAndConditionsCheckbox = self.page.locator('#CartDrawer-Form_agree')
        self.proceedToCheckoutButton = self.page.locator('a.tf-btn.btn-fill.animate-hover-btn.radius-3.w-100.justify-content-center[href="/checkout"]')
        self.fieldFirstName = self.page.locator("#first-name")
        self.fieldLastName = self.page.locator("#last-name")
        self.fieldCountry = self.page.locator("#country")
        self.fieldCity = self.page.locator("#city")
        self.fieldAdress = self.page.locator("#address")
        self.fieldPhoneNumber = self.page.locator("#phone")
        self.fieldEmail = self.page.locator("#email")
        self.fieldDiscountCode = self.page.locator('.coupon-box input[placeholder="Discount code"]')
        self.discontCodeButton = self.page.locator("a.tf-btn btn-sm radius-3 btn-fill btn-icon animate-hover-btn")
        self.fieldCardNumber = self.page.locator("#wrapper > section > div > div > div.tf-page-cart-footer > div > form > div.coupon-box.mb_20 > input[type=text]")
        self.fieldCardExpiration = self.page.locator("#wrapper > section > div > div > div.tf-page-cart-footer > div > form > div.box.grid-2 > div:nth-child(1) > input[type=text]")
        self.fieldCardCVV = self.page.locator("#wrapper > section > div > div > div.tf-page-cart-footer > div > form > div.box.grid-2 > div:nth-child(2) > input[type=text]")
        self.agreeCheckbox = self.page.locator("#check-agree")
        self.placeOrderButton = self.page.locator("#wrapper > section > div > div > div.tf-page-cart-footer > div > form > button")

    async def clickTermsAndConditionsCheckbox(self):
        assert self.termsAndConditionsCheckbox, "No terms and conditions checkbox found"
        await self.termsAndConditionsCheckbox.click()
    
    async def clickProceedToCheckoutButton(self):
        assert self.proceedToCheckoutButton, "No proceed to checkout button found"
        await self.proceedToCheckoutButton.click()

    async def fillFirstName(self, first_name):
        assert self.fieldFirstName, "No first name field found"
        await self.fieldFirstName.fill(first_name)

    async def fillLastName(self, last_name):
        assert self.fieldLastName, "No last name field found"
        await self.fieldLastName.fill(last_name)
    
    async def fillCountry(self, country_value=None):
        assert self.fieldCountry, "No country field found"
        if country_value:
            await self.page.select_option("#country", value=country_value)
        else:
            # Selecciona la primera opción (índice 0)
            await self.page.select_option("#country", index=0)

    async def fillCity(self, city): 
        assert self.fieldCity, "No city field found"
        await self.fieldCity.fill(city)

    async def fillAdress(self, adress):
        assert self.fieldAdress, "No adress field found"
        await self.fieldAdress.fill(adress) 

    async def fillPhoneNumber(self, phone_number):  
        assert self.fieldPhoneNumber, "No phone number field found"
        await self.fieldPhoneNumber.fill(phone_number)  

    async def fillEmail(self, email):
        assert self.fieldEmail, "No email field found"
        await self.fieldEmail.fill(email)   

    async def fillDiscountCode(self, discount_code):    
        assert self.fieldDiscountCode, "No discount code field found"
        await self.fieldDiscountCode.fill(discount_code)
    
    async def fillCardNumber(self, card_number):
        assert self.fieldCardNumber, "No card number field found"
        await self.fieldCardNumber.fill(card_number)

    async def fillCardExpiration(self, card_expiration):
        assert self.fieldCardExpiration, "No card expiration field found"
        await self.fieldCardExpiration.fill(card_expiration)    

    async def fillCardCVV(self, card_cvv):  
        assert self.fieldCardCVV, "No card CVV field found"
        await self.fieldCardCVV.fill(card_cvv)

    async def clickAgreeCheckbox(self):
        assert self.agreeCheckbox, "No agree checkbox found"
        await self.agreeCheckbox.click()
    
    async def clickPlaceOrderButton(self):
        assert self.placeOrderButton, "No place order button found"
        await self.placeOrderButton.click()

    
