from utils.appium_mobile import AppiumMobile
import allure

class Reporter(AppiumMobile):

    def screenshot_allure(self, str_descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), str_descripcion, attachment_type=allure.attachment_type.PNG)
