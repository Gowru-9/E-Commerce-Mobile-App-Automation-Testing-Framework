from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.config import (
    PLATFORM_NAME,
    AUTOMATION_NAME,
    DEVICE_NAME,
    APP_PACKAGE,
    APP_ACTIVITY,
    APPIUM_SERVER_URL,
    NO_RESET
)


def create_driver():

    options = UiAutomator2Options()

    options.platform_name = PLATFORM_NAME
    options.automation_name = AUTOMATION_NAME
    options.device_name = DEVICE_NAME

    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY

    options.no_reset = NO_RESET
    options.new_command_timeout = 120

    driver = webdriver.Remote(
        APPIUM_SERVER_URL,
        options=options
    )

    return driver