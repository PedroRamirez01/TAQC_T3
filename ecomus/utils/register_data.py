from models.register_user import RegisterUser

# Data for test_register.py
register_valid_users = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RVU1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RVU2@hotmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RVU3@outlook.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RVU4@live.es", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RVU5@yahoo.com", password="StrongPass123"),
]

register_empty_field_firstname = [
    RegisterUser(first_name="", last_name="Lastname", email="team_3_REFF1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name=" ", last_name="Lastname", email="team_3_REFF2@gmail.com", password="StrongPass123"),
]

register_empty_field_lastname = [
    RegisterUser(first_name="Firstname", last_name="", email="team_3_REFL1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name=" ", email="team_3_REFL2@gmail.com", password="StrongPass123"),
]

register_empty_field_email = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email=" ", password="StrongPass123"),
]

register_empty_field_password = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_REFU4@gmail.com", password=""),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_REFU4@gmail.com", password=" "),
]

register_invalid_firstname_users = [
    RegisterUser(first_name="#", last_name="Lastname", email="team_3_RIFU1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="$.", last_name="Lastname", email="team_3_RIFU2@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="!$#%", last_name="Lastname", email="team_3_RIFU3@gmail.com", password="StrongPass123"),
]

register_invalid_lastname_users = [
    RegisterUser(first_name="Firstname", last_name="$", email="team_3_RILU1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="#.", email="team_3_RIFU2@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="!$%&", email="team_3_RIFU3@gmail.com", password="StrongPass123"),
]

register_invalid_email_users = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="@", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIEU5", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIEU6@gmailcom", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIEU6@gmail.......com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="@gmailcom", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="@gmail.com", password="StrongPass123"),
]

register_invalid_password_users = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIPU1@gmail.com", password="aaaaaaaaaaaaaaaaaaaaaaa"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_RIPU2@gmail.com", password="1"),
]

register_user_already_create = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="olduser@gmail.com", password="oldpassword"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="olduser2@gmail.com", password="oldpassword2"),
]