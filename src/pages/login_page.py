
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from utils.reporter import Reporter


class LoginPage(BasePage):
    USUARIO = "//*[contains(@resource-id,'txtUsuario')]"
    PASSWORD = "//*[contains(@resource-id,'txtPassword')]"
    INGRESAR = "//*[contains(@resource-id,'btnLogin')]"
    LOGIN_EXITOSO = "//*[contains(@resource-id,'parentPanel')]"
    OK = "//*[contains(@resource-id,'button1')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 7)

    def ec_wait(self, locator):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def find_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)

    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def verificar_login_exitoso(self):
        try:
            self.find_element(self.LOGIN_EXITOSO)
        except NoSuchElementException:
            assert False, (f'El elemento: {self.LOGIN_EXITOSO} no existe en la app')
        else:
            assert True, (f'El elemento: {self.LOGIN_EXITOSO}  existe en la página')
    def login_exitoso(self, str_usuario, str_password):
        self.ec_wait(self.USUARIO)
        self.send_keys(self.USUARIO, str_usuario)
        self.send_keys(self.PASSWORD, str_password)
        self.click(self.INGRESAR)
        self.ec_wait(self.LOGIN_EXITOSO)
        self.verificar_login_exitoso()
        self.click(self.OK)
        Reporter.screenshot_allure(self, "Evidence")


