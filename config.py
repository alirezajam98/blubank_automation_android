import os
import datetime
import logging


# پیکربندی لاگ‌ها
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("test_log.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levellevelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


# ایجاد دایرکتوری برای ذخیره اسکرین‌شات‌ها
def create_screenshot_directory(device_name):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    directory_name = f"{device_name}_{timestamp}"
    base_dir = os.path.join(os.getcwd(), 'screenshots')
    full_path = os.path.join(base_dir, directory_name)
    os.makedirs(full_path, exist_ok=True)
    return full_path


# گرفتن اسکرین‌شات
def take_screenshot(driver, path, test_name):
    filename = f"{test_name}.png"
    full_path = os.path.join(path, filename)
    driver.save_screenshot(full_path)
