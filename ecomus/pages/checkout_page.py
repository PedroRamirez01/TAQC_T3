from playwright.async_api import Page, expect
from config.config import Config

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
        self.url = Config.URL_BASE
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

    async def navigate(self) -> None:
        """Navigates to the HomePage."""
        await self.page.goto(self.url, wait_until="domcontentloaded")
        await expect(self.page).to_have_url(self.url)

    async def clickTermsAndConditionsCheckbox(self):
        await expect(self.termsAndConditionsCheckbox).to_be_visible()
        await self.termsAndConditionsCheckbox.click()
    
    async def clickProceedToCheckoutButton(self):
        await expect(self.proceedToCheckoutButton).to_be_visible()
        await self.proceedToCheckoutButton.click()

    async def fillFirstName(self, first_name):
        await expect(self.fieldFirstName).to_be_visible()
        await self.fieldFirstName.fill(first_name)

    async def fillLastName(self, last_name):
        await expect(self.fieldLastName).to_be_visible()
        await self.fieldLastName.fill(last_name)
    
    async def fillCountry(self, country_value=None):
        await expect(self.fieldCountry).to_be_visible()
        if country_value:
            await self.page.select_option("#country", value=country_value)
        else:
            await self.page.select_option("#country", index=0)

    async def fillCity(self, city): 
        await expect(self.fieldCity).to_be_visible()
        await self.fieldCity.fill(city)

    async def fillAdress(self, adress):
        await expect(self.fieldAdress).to_be_visible()
        await self.fieldAdress.fill(adress) 

    async def fillPhoneNumber(self, phone_number):  
        await expect(self.fieldPhoneNumber).to_be_visible()
        await self.fieldPhoneNumber.fill(phone_number)  

    async def fillEmail(self, email):
        await expect(self.fieldEmail).to_be_visible()
        await self.fieldEmail.fill(email)   

    async def fillDiscountCode(self, discount_code):    
        await expect(self.fieldDiscountCode).to_be_visible()
        await self.fieldDiscountCode.fill(discount_code)
    
    async def fillCardNumber(self, card_number):
        await expect(self.fieldCardNumber).to_be_visible()
        await self.fieldCardNumber.fill(card_number)

    async def fillCardExpiration(self, card_expiration):
        await expect(self.fieldCardExpiration).to_be_visible()
        await self.fieldCardExpiration.fill(card_expiration)    

    async def fillCardCVV(self, card_cvv):  
        await expect(self.fieldCardCVV).to_be_visible()
        await self.fieldCardCVV.fill(card_cvv)

    async def clickAgreeCheckbox(self):
        await expect(self.agreeCheckbox).to_be_visible()
        await self.agreeCheckbox.click()
    
    async def clickPlaceOrderButton(self):
        await expect(self.placeOrderButton).to_be_visible()
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
            Extract the order ID from the success message.
            :return: The order ID as a string.
            """
            order_text = await self.successMessage.text_content()
            return order_text.split("Your order ID is: ")[1].strip()
        except Exception as e:
            print(f"[ERROR] No se pudo extraer el ID de orden: {e}")
            return None

    async def getOrderbyId(self, order_id):
        """
        Consults the order by ID from the API and returns the content if it exists.
        """
        if not order_id:
            print("[ERROR] El ID de orden está vacío.")
            return None

        try:
            response = await self.page.request.get(f"{Config.URL_BASE}api/orders/{order_id}")
            if response.ok:
                return await response.json()
            else:
                print(f"[ERROR] Order not found (status {response.status})")
                return None
        except Exception as e:
            print(f"[ERROR] Fail to obtain the order: {e}")
            return None

