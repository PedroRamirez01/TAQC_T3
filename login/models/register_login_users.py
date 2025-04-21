from dataclasses import dataclass
from models.register_user import RegisterUser
from models.login_user import LoginUser

@dataclass
class RegisterLoginUser:
    """_summary_
    RegisterLoginUser dataclass to hold user registration and login information.
    Attributes:
        register (RegisterUser): The registration information of the user.
        login (LoginUser): The login information of the user.
    """

    register: RegisterUser
    login: LoginUser