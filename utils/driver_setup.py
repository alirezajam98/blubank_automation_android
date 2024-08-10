from appium import webdriver
from appium.options.android import UiAutomator2Options
import json


def get_driver(device_name):
    with open('devices.json') as f:
        devices = json.load(f)
    device_info = devices[device_name]

    # استفاده از UiAutomator2Options برای تنظیمات دستگاه
    options = UiAutomator2Options()
    options.platform_name = device_info['platformName']
    options.device_name = device_info['deviceName']
    options.udid = device_info['udid']
    options.platform_version = device_info.get('platformVersion', '12.0.0')
    options.automation_name = device_info['automationName']
    options.app_package = device_info['appPackage']
    options.app_activity = device_info['appActivity']

    server_url = 'http://127.0.0.1:4723'  # بدون /wd/hub
    driver = webdriver.Remote(server_url, options=options)

    return driver
