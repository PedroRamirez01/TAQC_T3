from models.register_user import RegisterUser
from models.login_user import LoginUser
from models.register_login_users import RegisterLoginUser

# Data for test_register.py
register_valid_users = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RVU1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RVU2@hotmail.com", password="AnotherStrong123"),
]

register_empty_fields_users = [
    RegisterUser(first_name="", last_name="Lastname", email="team_3_REFU1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="", email="team_3_REFU2@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_REFU4@gmail.com", password=""),
]

register_invalid_email_users = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="@", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIEU5", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIEU6@gmailcom", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIEU6@gmail.......com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="@gmail.com", password="StrongPass123"),
]

register_invalid_firstname_users = [
    RegisterUser(first_name="#", last_name="Lastname", email="team_3_RIFU1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="$", last_name="Lastname", email="team_3_RIFU2@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="!$#%", last_name="Lastname", email="team_3_RIFU3@gmail.com", password="StrongPass123"),
]

register_invalid_lastname_users = [
    RegisterUser(first_name="Firstname", last_name="$", email="team_3_RILU1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="#", email="team_3_RIFU2@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="!$%&", email="team_3_RIFU3@gmail.com", password="StrongPass123"),
]

register_invalid_password_users = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIPU1@gmail.com", password="aaaaaaaaaaaaaaaaaaaaaaa"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIPU2@gmail.com", password="1"),
]

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