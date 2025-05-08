import re
from playwright.async_api import Page, expect
from utils.api_requests import verify_order_exists

class CheckoutPage:

    """
    Page Object Model for the checkout page.
    Allows filling out the checkout form, applying discount codes, and placing an order.
    """

    def __init__(self, page: Page):
        """
        Initializes locators for the checkout functionalities.
        :param page: Instance of Playwright Page.
        """
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
        self.successMessage = self.page.locator('p[style*="color: green"]:has-text("Order saved successfully!")')

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

    async def fillCheckoutForm(self, data):
        await self.fillFirstName(data["FIRST_NAME"])
        await self.fillLastName(data["LAST_NAME"])
        await self.fillCountry(data["COUNTRY"])
        await self.fillCity(data["CITY"])
        await self.fillAdress(data["ADDRESS"])
        await self.fillPhoneNumber(data["PHONE_NUMBER"])
        await self.fillEmail(data["EMAIL"])  
        await self.fillDiscountCode(data["DISCOUNT_CODE"])
        await self.fillCardNumber(data["CARD_NUMBER"])
        await self.fillCardExpiration(data["CARD_EXPIRATION"])
        await self.fillCardCVV(data["CARD_CVV"])

    async def getOrderId(self):
        try:
            """
            Extracts the order ID (UUID) from the success message after placing the order.
            :return: The extracted order ID string.
            """
            order_text = await self.successMessage.text_content()
            match = re.search(r"[a-f0-9\-]{36}", order_text)
            if match:
                return match.group(0)
            else:
                raise ValueError("Order ID not found in the success message.")
        except Exception as e:
            print(f"[ERROR] No se pudo extraer el ID de orden: {e}")
            return None
        
    async def assertOrderInApi(self, order_id):
        """
        Asserts whether the order ID exists in the API.
        :param order_id: The order ID to check.
    
        """
        if order_id:
            exists = await verify_order_exists(order_id)    
            assert exists, f"Order with ID {order_id} does not exist in the API"
        else:
            pass


    async def assertSuccessMessage(self, label, order_id):
        """
        Asserts whether the success message appears based on the label.
        :param label: Describes if it is a 'valid' or 'invalid' checkout.
        """
        if label.startswith("valid"):
            await expect(self.successMessage).to_be_visible()
            assert order_id, "Expected an order ID for a valid checkout"
        else:
            await expect(self.successMessage).not_to_be_visible()
            assert not order_id, "Expected no order ID for an invalid checkout"

    
