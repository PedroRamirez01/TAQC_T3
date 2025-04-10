from models.register_user import RegisterUser

register_valid_users = [
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_valid1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_valid2@gmail.com", password="AnotherStrong123"),
]

register_invalid_users = [
    RegisterUser(first_name="", last_name="Lastname", email="team_3_invalid1@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_invalid2@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_invalid4@gmail.com", password=""),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_invalid5@gmail.com", password="StrongPass123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_invalid6", password="123"),
    RegisterUser(first_name="Firstname", last_name="Lastname", email="team_3_invalid7", password="LooooooooooooooooooooooooongPassword"),
]

