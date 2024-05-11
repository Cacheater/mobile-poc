
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from utils.initialize import Initialize
from utils.appium_mobile import AppiumMobile
from utils.reporter import Reporter


def before_scenario(context, scenario):
    AppiumMobile.open_mobile(context, device=Initialize.DEVICE, app_type=Initialize.APP_TYPE)

def after_step(context, scenario):
    if scenario.status == 'failed':
        Reporter.screenshot_allure(context, "Algo salió mal")
        AppiumMobile.end_app(context)


def before_feature(context, feature):
    for scenario in feature.scenarios:
        if "ttf" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=2)

