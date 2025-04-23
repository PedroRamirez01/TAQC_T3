from playwright.async_api import Page
from models.login_user import LoginUser
from config.config import Config

class LoginPage:
    """_summary_
    Clase que representa la página de inicio de sesión.
    Contiene métodos para navegar a la página, completar los campos de inicio de sesión y enviar el formulario.
    Atributos:
        url (str): URL de la página de inicio de sesión.
        page (Page): Instancia de la página de Playwright.
        field_email (Locator): Campo de entrada para el correo electrónico.
        field_password (Locator): Campo de entrada para la contraseña.
        btn_login (Locator): Botón para enviar el formulario de inicio de sesión.
    Métodos:
        navigate(): Navega a la página de inicio de sesión.
        fill_email(email: str): Completa el campo de correo electrónico.
        fill_password(password: str): Completa el campo de contraseña.
        submit(): Envía el formulario de inicio de sesión.
        login(user: LoginUser): Realiza el inicio de sesión con un usuario dado.
    """

    def __init__(self, page: Page):
        self.url = Config.URL_LOGIN_PAGE
        self.page = page
        self.field_email = page.locator("#loginEmail")
        self.field_password = page.locator("#loginPassword")
        self.btn_login = page.locator("#login > div > form > div:nth-child(4) > button")

    async def navigate(self) -> None:
        await self.page.goto(self.url, wait_until="domcontentloaded")

    async def fill_email(self, email: str) -> None:
        await self.field_email.fill(email)

    async def fill_password(self, password: str) -> None:
        await self.field_password.fill(password)

    async def submit(self) -> None:
        await self.btn_login.click()

    async def login(self, user: LoginUser) -> None:
        await self.navigate()
        await self.fill_email(user.email)
        await self.fill_password(user.password)
        await self.submit()
        await self.page.wait_for_timeout(2000)
