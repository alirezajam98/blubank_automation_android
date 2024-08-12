import pytest
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options


def pytest_addoption(parser):
    parser.addoption("--device", action="store", default=None)


@pytest.fixture(scope='function')
def create_driver_fixture(request):
    device_name = request.config.getoption("--device")

    with open('test_config.json') as f:
        devices = json.load(f)["devices"]

    device_info = devices[device_name]

    options = UiAutomator2Options()
    options.platform_name = device_info['platformName']
    options.device_name = device_info['deviceName']
    options.udid = device_info['udid']
    options.platform_version = device_info['platformVersion']
    options.automation_name = device_info['automationName']
    options.app_package = device_info['appPackage']
    options.app_activity = device_info['appActivity']

    server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(server_url, options=options)

    driver.implicitly_wait(10)  # اضافه کردن implicit wait

    yield driver
    driver.quit()
