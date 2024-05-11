import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from utils.reporter import Reporter

class Registros(BasePage):

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

    def verificar_registro(self, registro):
        try:
            reg_gherkin = "//*[contains(@text,'{}')]".format(registro)
            self.ec_wait(reg_gherkin)
            self.find_element(reg_gherkin)
            Reporter.screenshot_allure(self, "Evidence")
        except NoSuchElementException:
            assert False, (f'El elemento: {reg_gherkin} no existe en la app')

        else:
            assert True, (f'El elemento: {reg_gherkin}  existe en la página')
