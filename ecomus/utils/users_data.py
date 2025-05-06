from models.register_user import RegisterUser
from models.login_user import LoginUser
from models.register_login_users import RegisterLoginUser

# Data for test_login.py
login_valid_users = [
    LoginUser(email="olduser@gmail.com", password="oldpassword"),
]

login_no_register_users = [
    LoginUser(email="not_register_email@gmail.com", password="not_register_email"),
    LoginUser(email="not_register_email@gmail", password="not_register_email"),
    LoginUser(email="not_register_email@gmail....com", password="not_register_email"),
]

login_user_invalid_email = [
    LoginUser(email="invalid_user@gmailcom", password="invalid_password"),
    LoginUser(email="invalid_user@gmail", password="invalid_password"),
    LoginUser(email="invalid_user@gmail....com", password="invalid_password"),
]

login_user_empty_email = [
    LoginUser(email="", password="valid_password"),
    LoginUser(email=" ", password="valid_password"),
]

login_user_empty_password = [
    LoginUser(email="olduser@gmail.com", password=""),
    LoginUser(email="olduser@gmail.com", password=" "),
]

#Data for test_register_login.py
register_login_valid_new_users = [
    RegisterLoginUser(
        register=RegisterUser(
            first_name="Firstname",
            last_name="Lastname",
            email="team_3_RLVU1@gmail.com",
            password="StrongPass123"
        ),
        login=LoginUser(
            email="team_3_RLVU1@gmail.com",
            password="StrongPass123"
        )
    ),
    RegisterLoginUser(
        register=RegisterUser(
            first_name="Firstname",
            last_name="Lastname",
            email="team_3_RLVU2@gmail.com",
            password="StrongPass123"
        ),
        login=LoginUser(
            email="team_3_RLVU2@gmail.com",
            password="StrongPass123"
        )
    ),
]

register_login_invalid_new_users = [
    RegisterLoginUser(
        register=RegisterUser(
            first_name="Firstname",
            last_name="Lastname",
            email="team_3_RLIU1@gmailcom",
            password="StrongPass123"),
        login=LoginUser(
            email="team_3_RLVU1@gmailcom",
            password="StrongPass123")
    ),
    RegisterLoginUser(
        register=RegisterUser(
            first_name="Firstname",
            last_name="Lastname",
            email="team_3_RLIU2@gmail.com",
            password="1"),
        login=LoginUser(
            email="team_3_RLVU2@gmail.com",
            password="1")
    ),
]

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