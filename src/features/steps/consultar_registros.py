from pages.login_page import LoginPage
from pages.menu_home_page import MenuHomePage
from utils.appium_mobile import AppiumMobile
from pages.registros import Registros
from behave import *

use_step_matcher("re")

class Consultar_Registros:

    def __init__(self):
        self.driver = None

    @given("Inicio sesión en la app con un usuario valido (?P<usuario>.+)")
    def step_impl(context, usuario):
        login_page = LoginPage(context.driver)
        login_page.login_exitoso(usuario, "Test1234")

    @when("Consulto los registro existentes")
    def step_impl(context):
        menu_home_page = MenuHomePage(context.driver)
        menu_home_page.click_on_consultar_registros()

    @then("Verifico que se se muestre eel registro: (.*)")
    def step_impl(context, registro):
        AppiumMobile.scroll_down(context, 500)
        registros = Registros(context.driver)
        registros.verificar_registro(registro)
        AppiumMobile.end_app(context)


