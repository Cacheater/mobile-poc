from selenium.common import NoSuchElementException

from utils.reporter import Reporter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class MenuHomePage(BasePage):

    CONSULTAR_REGISTRO = "//*[contains(@resource-id,'btnConsultarRegistros')]"
    TITULO_PAGINA = "//*[contains(@resource-id,'lblWelcome')]"

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

    def verificar_objeto_existe(self):
        try:
            self.ec_wait(self.CONSULTAR_REGISTRO)
            self.find_element(self.CONSULTAR_REGISTRO)
            Reporter.screenshot_allure(self, "Evidence")
        except NoSuchElementException:
            assert False, (f'El elemento: {self.TITULO_PAGINA} no existe en la app')
        else:
            assert True, (f'El elemento: {self.TITULO_PAGINA}  existe en la página')

    def click_on_consultar_registros(self):
        self.ec_wait(self.CONSULTAR_REGISTRO)
        self.click(self.CONSULTAR_REGISTRO)
        Reporter.screenshot_allure(self, "Evidence")

