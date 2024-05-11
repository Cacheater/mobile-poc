import os

from utils.initialize import Initialize
from appium import webdriver
from utils.rw_json import GetJson


class AppiumMobile():
    def open_mobile(context, device=Initialize.DEVICE, app_type=Initialize.APP_TYPE):
        caps = {}
        print(Initialize.basedir)
        print("*************************")
        print(device)
        print("*************************")

        # GET DATA DEVICE
        GetJson.get_json_file(context)
        device_data = GetJson.get_device(context, device)

        # ****************************************************************
        # CAPABILITIES - KOBITON SESION DATA
        # ****************************************************************

        caps['sessionName'] = device_data['kobiton_sesion']['sessionName'] + " - " + device.upper()
        caps['sessionDescription'] = device_data['kobiton_sesion']['sessionDescription']
        caps['deviceOrientation'] = device_data['kobiton_sesion']['deviceOrientation']
        caps['captureScreenshots'] = device_data['kobiton_sesion']['captureScreenshots']
        caps['deviceGroup'] = device_data['kobiton_sesion']['deviceGroup']
        caps['groupId'] = device_data['kobiton_sesion']['groupId']

        # ****************************************************************
        # CAPABILITIES - DEVICE DATA
        # ****************************************************************
        caps['udid'] = device_data['udid']
        caps['platformName'] = device_data['platformName']
        caps['automationName'] = device_data['automationName']
        caps['platformVersion'] = device_data['platformVersion']
        caps['appPackage'] = device_data['appPackage']
        caps['appActivity'] = device_data['appActivity']
        #caps['appWaitActivity'] = device_data['appWaitActivity']
        #caps['appWaitPackage'] = device_data['appWaitPackage']
        caps['appWaitDuration'] = device_data['appWaitDuration']
        caps['appWaitForLaunch'] = device_data['appWaitForLaunch']

        # ****************************************************************
        # CAPABILITIES - APP TYPE
        # ****************************************************************
        STR_APP_NATIVE = "APP_NATIVE"
        STR_WEB_MOBILE = "WEB_MOBILE"
        STR_APP_STACK = "STACK"
        app_type_upper = app_type.upper()

        if app_type_upper == STR_APP_STACK:
            caps['app'] = device_data['app']

        elif app_type_upper == STR_WEB_MOBILE:
            if device_data['platformName'].upper == 'ANDROID':
                caps['browserName'] = device_data['browserName']
                caps['chromedriverExecutable'] = device_data['chromedriverExecutable']
            elif device_data['platformName'].upper == 'IOS':
                caps['browserName'] = device_data['browserName']

        # ****************************************************************
        # CAPABILITIES - OTHERS
        # ****************************************************************
        caps['noReset'] = device_data['noReset']
        caps['fullReset'] = device_data['fullReset']
        caps['adbExecTimeout'] = device_data['adbExecTimeout']
        caps['newCommandTimeout'] = device_data['newCommandTimeout']

        context.driver = webdriver.Remote(device_data['setup']['url_appium_server'], caps)
        return context.driver

    # *****************************************************************************************
    # DRIVER - GENERIC
    # *****************************************************************************************

    def tear_down(context):
        # oReporter.fn_screenshot_allure(self, "Ultimo paso antes de cerrar el driver")
        print("Se cierra la coneccion con el Driver")
        context.driver.quit()

    def tear_down_driver(context):
        print("Se cierra la coneccion con el Driver")
        context.driver.close()
        context.driver.quit()

    def get_session_id(context):
        return context.driver.session_id()

    def get_driver(context):
        return context.driver

    # *****************************************************************************************
    # DRIVER - BROWSER MOBILE
    # *****************************************************************************************

    def get_title(context):
        return context.driver.title

    def refresh_driver(context):
        return context.driver.refresh()

    def get_url(context):
        return context.driver.current_url

    def set_url(context, url):
        return context.driver.get(url)

    # *****************************************************************************************
    # DRIVER - DEVICE
    # *****************************************************************************************

    def hide_keyboard(context):
        return context.driver.hide_keyboard()

    def end_app(context):
        print("Se cierra la conexión con el driver")
        context.driver.terminate_app('com.mate_app')
        context.driver.quit()

    def scroll_down(context, scroll_size=None):
        scroll_size = 100 if scroll_size == None else int(scroll_size)

        try:
            screen_size = context.driver.get_window_size()
            x1 = screen_size['width'] / 2
            x2 = screen_size['width'] / 2
            y1 = screen_size['height'] / 2
            y2 = y1 - scroll_size

            context.driver.swipe(x1, y1, x2, y2)

        except Exception as e:
            print("Error. Al hacer Scroll Down. Exception: " + e)

    def scroll_up(context, scroll_size=None):
        scroll_size = 100 if scroll_size == None else float(scroll_size)

        try:
            screen_size = context.driver.get_window_size()
            x1 = screen_size['width'] / 2
            x2 = screen_size['width'] / 2
            y1 = screen_size['height'] / 2
            y2 = y1 + scroll_size

            context.driver.swipe(x1, y1, x2, y2)

        except Exception as e:
            print("Error. Al hacer Scroll Down. Exception: " + e)