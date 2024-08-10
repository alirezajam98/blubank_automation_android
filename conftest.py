import datetime
import pytest
from utils.driver_setup import get_driver
import os

def pytest_addoption(parser):
    parser.addoption("--device", action="store", default="device1")

@pytest.fixture(scope='module')
def create_driver_fixture(request):
    device_name = request.config.getoption("--device")
    driver = get_driver(device_name)
    yield driver
    driver.quit()



def create_screenshot_directory(device_name):
    # دریافت تاریخ و زمان فعلی
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # ساختن نام دایرکتوری با فرمت: deviceName_YYYY-MM-DD_HH-MM-SS
    directory_name = f"{device_name}_{timestamp}"

    # مسیر دایرکتوری اسکرین‌شات‌ها
    base_dir = os.path.join(os.getcwd(), 'screenshots')

    # ایجاد مسیر کامل
    full_path = os.path.join(base_dir, directory_name)
    os.makedirs(full_path, exist_ok=True)

    return full_path


def take_screenshot(driver, path, filename):
    full_path = os.path.join(path, f"{filename}.png")
    driver.save_screenshot(full_path)
