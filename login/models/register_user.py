from dataclasses import dataclass

@dataclass
class RegisterUser:
    first_name: str
    last_name: str
    email: str
    password: str