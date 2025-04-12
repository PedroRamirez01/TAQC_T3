from dataclasses import dataclass
from models.register_user import RegisterUser
from models.login_user import LoginUser

@dataclass
class RegisterLoginUser:
    register: RegisterUser
    login: LoginUser