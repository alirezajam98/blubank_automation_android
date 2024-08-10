import datetime
import pytest
from utils.driver_setup import get_driver
import os
import logging
def pytest_addoption(parser):
    parser.addoption("--device", action="store", default="device1")

@pytest.fixture(scope='module')
def create_driver_fixture(request):
    device_name = request.config.getoption("--device")
    driver = get_driver(device_name)
    yield driver
    driver.quit()


# پیکربندی دایرکتوری اسکرین‌شات‌ها
def create_screenshot_directory(device_name):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    directory_name = f"{device_name}_{timestamp}"
    base_dir = os.path.join(os.getcwd(), 'screenshots')
    full_path = os.path.join(base_dir, directory_name)
    os.makedirs(full_path, exist_ok=True)
    return full_path


def take_screenshot(driver, path, test_name):
    filename = f"{test_name}.png"
    full_path = os.path.join(path, filename)
    driver.save_screenshot(full_path)


# پیکربندی لاگینگ
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("test_log.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger