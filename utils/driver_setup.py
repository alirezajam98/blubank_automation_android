import os
import datetime

def create_screenshot_directory(base_dir="screenshots"):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    full_path = os.path.join(base_dir, timestamp)
    os.makedirs(full_path, exist_ok=True)
    return full_path

def save_screenshot(driver, base_dir, device_name, udid, test_name):
    directory = os.path.join(base_dir, f"{device_name}_{udid}")
    os.makedirs(directory, exist_ok=True)
    screenshot_path = os.path.join(directory, f"{test_name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
