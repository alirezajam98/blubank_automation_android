import logging

import pytest
from conftest import setup_logging, create_screenshot_directory, take_screenshot
from pages.HomePage import HomePage
from pages.Login.Login_page import LoginPage
from pages.Login.BiometricPage import Biometric
from pages.Login.Notif_BottomSheet import Notif_BottomSheet
from selenium.common.exceptions import NoSuchElementException, TimeoutException

logger = setup_logging()


@pytest.mark.smoke
@pytest.mark.run(order=3)
def test_login_with_biometric(create_driver_fixture, caplog):
    driver = create_driver_fixture
    device_name = driver.capabilities['deviceName']

    # ایجاد دایرکتوری برای ذخیره اسکرین‌شات‌ها
    screenshot_dir = create_screenshot_directory(device_name)

    with caplog.at_level(logging.INFO):
        logger.info(f"Running test on device: {device_name}")

        try:
            login_page = LoginPage(driver)
            login_page.enter_username('recap8')
            login_page.enter_password('Aa123456')
            logger.info(f"Entered username and password on device: {device_name}")

            biometric_page = login_page.press_login_button()
            logger.info(f"Clicked on login button on device: {device_name}")

            assert biometric_page.is_btn_not_now_displayed(), "Biometric page should be displayed after login"
            logger.info(f"Biometric page displayed after login on device: {device_name}")

            biometric_page.click_btn_not_now()
            logger.info(f"Clicked on 'Not Now' button on device: {device_name}")

            notif_BottomSheet = Notif_BottomSheet(driver)
            if notif_BottomSheet.is_permission_button_displayed():
                notif_BottomSheet.click_permission_button()
                logger.info(f"Clicked on permission button on device: {device_name}")

            home_page = HomePage(driver)
            assert home_page.get_welcome_message() == "خانه"
            logger.info(f"Verified welcome message on device: {device_name}")

        except (NoSuchElementException, TimeoutException, AssertionError) as e:
            logger.error(f"Error during steps on device: {device_name} - {str(e)}")
            take_screenshot(driver, screenshot_dir, "test_login_with_biometric")
            pytest.fail(f"Test failed on device: {device_name}")
