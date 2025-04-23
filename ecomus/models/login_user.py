from dataclasses import dataclass

@dataclass
class LoginUser:
    """_summary_
    LoginUser dataclass to hold user login information.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
    """

    email: str
    password: str