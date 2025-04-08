import time
from playwright.async_api import Page

class AddProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.selectItem = page.locator("div.card-product:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(2)")
        self.addItems = page.locator("div.tf-product-info-quantity:nth-child(7) > div:nth-child(2) > span:nth-child(3)")
        self.addToCart = page.locator("div.tf-product-info-buy-button:nth-child(8) > form:nth-child(1) > a:nth-child(1)")
        self.cart = page.locator(".btn-outline")
