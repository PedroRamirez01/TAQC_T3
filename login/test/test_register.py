import pytest
from utils.users_data import register_valid_users, register_invalid_users

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user", register_valid_users
)
async def test_valid_registrations(register_page, user, delete_user):
    await register_page.register(user)
    assert "/login" in register_page.page.url, f"Usuario Valido no creado: {user}"
    delete_user(user.email)

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user", register_invalid_users
)
async def test_invalid_registrations(register_page, user, delete_user):
    await register_page.register(user)
    assert "/register" in register_page.page.url, f"Se creó un usuario inválido: {user}"
    delete_user(user.email)

# Total pruebas: 7
# Prueba 1: Registro exitoso
# Prueba 2: Registro con 'Email' inválido
# Prueba 3: Registro con 'Password' que no cumple requisitos minimos de seguridad
# Prueba 4: Registro con 'First name' vacío
# Prueba 5: Registro con 'Last name' vacío
# Prueba 6: Registro con 'Email' vacío
# Prueba 7: Registro con 'Password' vacío
# Prueba 8: Registro con 'Email' existente

# @pytest.mark.asyncio
# async def test_successful_registration(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.USER_EMAIL,
#         Config.USER_PASSWORD
#         )
#     delete_user_by_id(Config.USER_EMAIL)
#     assert "/login" in register_page.page.url, "Usuario no registrado"

# @pytest.mark.asyncio
# async def test_registration_with_invalid_email(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.NEW_USER_INVALID_EMAIL,
#         Config.NEW_USER_INVALID_PASSWORD
#         )
#     delete_user_by_id(Config.NEW_USER_INVALID_EMAIL)
#     assert "/register" in register_page.page.url, "Se creo un usuario con email inválido"

# @pytest.mark.asyncio
# async def test_registration_with_invalid_password_security(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.NEW_USER_INVALID_EMAIL,
#         Config.NEW_USER_INVALID_PASSWORD
#         )
#     delete_user_by_id(Config.NEW_USER_INVALID_EMAIL)
#     assert "/register" in register_page.page.url, "Se creo un usuario con 'Password' que no cumple requisitos mínimos de seguridad"

# @pytest.mark.asyncio
# async def test_registration_with_empty_first_name(register_page):
#     await register_page.register(
#         "",
#         Config.USER_LAST_NAME,
#         Config.USER_EMAIL,
#         Config.USER_PASSWORD
#         )
#     assert "/register" in register_page.page.url, "Se creo un usuario sin email"

# @pytest.mark.asyncio
# async def test_registration_with_empty_last_name(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         "",
#         Config.USER_EMAIL,
#         Config.USER_PASSWORD
#         )
#     assert "/register" in register_page.page.url, "Se creo un usuario con 'Last name' vacío"

# @pytest.mark.asyncio
# async def test_registration_with_empty_email(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         "",
#         Config.USER_PASSWORD
#         )
#     assert "/register" in register_page.page.url, "Se creo un usuario con 'email' vacío"

# @pytest.mark.asyncio
# async def test_registration_with_empty_password(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.USER_EMAIL,
#         ""
#         )
#     assert "/register" in register_page.page.url, "Se creo un usuario con 'Password' vacío"

# @pytest.mark.asyncio
# async def test_registration_whit_existing_email(register_page):
#     await register_page.register(
#         Config.USER_FIRST_NAME,
#         Config.USER_LAST_NAME,
#         Config.OLD_USER_EMAIL,
#         Config.OLD_USER_PASSWORD
#         )
#     assert "/register" in register_page.page.url, "Se creo un usuario con email existente"