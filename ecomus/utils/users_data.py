from models.register_user import RegisterUser
from models.login_user import LoginUser
from models.register_login_users import RegisterLoginUser

# Data for test_product_detail.py
product_detail_quantity_input = [
    1, 3, 1000000000000000000000
]

product_detail_negative_quantity_input = [
    -1, -3, 0, -1000000000000000000000
]

product_detail_free_shipping = [
    1, 3, 10
]

product_detail_cart_close_cart = [
    1, 3, 4
]