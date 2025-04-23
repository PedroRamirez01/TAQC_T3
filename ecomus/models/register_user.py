from dataclasses import dataclass

@dataclass
class RegisterUser:
    """_summary_
    RegisterUser dataclass to hold user registration information.
    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email of the user.
        password (str): The password of the user.
    """

    first_name: str
    last_name: str
    email: str
    password: str