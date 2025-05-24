from models.register_user import RegisterUser
from models.login_user import LoginUser
from models.register_login_users import RegisterLoginUser

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