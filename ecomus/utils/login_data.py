from models.login_user import LoginUser

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