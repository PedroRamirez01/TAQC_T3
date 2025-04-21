from playwright.async_api import Page
import models.register_user as RegisterUser
from config.config import Config

class RegisterPage:
    """_summary_
    Clase que representa la página de registro en el sitio web de prueba.
    Proporciona métodos para interactuar con los elementos de la página y realizar el registro de un nuevo usuario.
    Atributos:
        url (str): URL de la página de registro.
        page (Page): Instancia de la página de Playwright.
        fieldFirstName (Locator): Localizador para el campo de nombre.
        fieldLastName (Locator): Localizador para el campo de apellido.
        fieldEmail (Locator): Localizador para el campo de correo electrónico.
        fieldPassword (Locator): Localizador para el campo de contraseña.
        btnRegister (Locator): Localizador para el botón de registro.
    Métodos:
        navigate(): Navega a la página de registro.
        fill_first_name(firstName: str): Rellena el campo de nombre.
        fill_last_name(lastName: str): Rellena el campo de apellido.
        fill_email(email: str): Rellena el campo de correo electrónico.
        fill_password(password: str): Rellena el campo de contraseña.
        submit(): Hace clic en el botón de registro.
        register(user: RegisterUser): Realiza el registro del usuario utilizando los datos proporcionados.
    """

    def __init__(self, page: Page) -> None:
        self.url = Config.URL_REGISTER_PAGE
        self.page = page
        self.fieldFirstName = self.page.locator("#register-form > div:nth-child(1) > input")
        self.fieldLastName = self.page.locator("input[name='lastName']")
        self.fieldEmail = self.page.locator("input[name='email'][placeholder=' ']")
        self.fieldPassword = self.page.locator("input[name='password']")
        self.btnRegister = self.page.locator("#register-form > div.mb_20 > button")

    async def navigate(self) -> None:
        await self.page.goto(self.url, wait_until="domcontentloaded")

    async def fill_first_name(self, firstName: str) -> None:
        await self.fieldFirstName.wait_for(state="visible")
        await self.page.screenshot(path="error_msg_register.png", full_page=True)
        await self.fieldFirstName.fill(firstName)

    async def fill_last_name(self, lastName: str) -> None:
        await self.fieldLastName.fill(lastName)

    async def fill_email(self, email: str) -> None:
        await self.fieldEmail.fill(email)
    
    async def fill_password(self, password: str) -> None:
        await self.fieldPassword.fill(password)

    async def submit(self) -> None:
        await self.btnRegister.click()

    async def register(self, user: RegisterUser) -> None:
        await self.navigate()
        await self.fill_first_name(user.first_name)
        await self.fill_last_name(user.last_name)
        await self.fill_email(user.email)
        await self.fill_password(user.password)
        await self.submit()
        await self.page.wait_for_timeout(3000)
