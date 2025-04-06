from playwright.async_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.termsAndConditionsCheckbox = self.page.locator('#CartDrawer-Form_agree')
        self.proceedToCheckoutButton = self.page.locator('a.tf-btn.btn-fill.animate-hover-btn.radius-3.w-100.justify-content-center[href="/checkout"]')

    def clickTermsAndConditionsCheckbox(self):
        assert self.termsAndConditionsCheckbox, "No terms and conditions checkbox found"
        return self.termsAndConditionsCheckbox.click()
    
    def clickProceedToCheckoutButton(self):
        assert self.proceedToCheckoutButton, "No proceed to checkout button found"
        return self.proceedToCheckoutButton.click()