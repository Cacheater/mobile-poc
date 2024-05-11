from pages.login_page import LoginPage
from pages.menu_home_page import MenuHomePage
from utils.appium_mobile import AppiumMobile
from behave import *

use_step_matcher("re")

class Iniciar_Sesion:
    def __init__(self):
        self.driver = None

    @given("Abro la app para poder iniciar sesion")
    def step_impl(context):
        pass


    @when("Inicio sesion con (?P<usuario>.+) y (?P<password>.+)")
    def step_impl(context, usuario, password):
        login_page = LoginPage(context.driver)
        login_page.login_exitoso(usuario, password)


    @then("Valido que se abra el home de la app")
    def step_impl(context):
        menu_home_page = MenuHomePage(context.driver)
        menu_home_page.verificar_objeto_existe()
        AppiumMobile.end_app(context)