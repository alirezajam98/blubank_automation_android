import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.HomePage import HomePage
from pages.Login.Login_page import LoginPage
from utils.driver_setup import create_screenshot_directory, save_screenshot


def test_login_with_biometric(create_driver_fixture, request):
    driver = create_driver_fixture
    device_name = request.config.getoption("--device")
    udid = driver.capabilities['udid']  # گرفتن UDID دستگاه
    screenshot_base_dir = create_screenshot_directory()

    try:
        # ایجاد یک شیء از کلاس LoginPage
        login_page = LoginPage(driver)

        # ورود نام کاربری و رمز عبور و کلیک روی دکمه ورود
        biometric_page = login_page.login('recap8', 'Aa123456')

        # بررسی اینکه آیا صفحه بیومتریک نمایش داده شده است
        assert biometric_page.is_btn_not_now_displayed(), "Biometric page should be displayed after login"

        # کلیک بر روی دکمه "Not Now"
        biometric_page.click_btn_not_now()

        # بررسی نمایش پیام خوش‌آمدگویی در صفحه اصلی
        home_page = HomePage(driver)
        assert home_page.get_welcome_message() == "خانه", "Welcome message not found!"

    except (NoSuchElementException, TimeoutException, AssertionError) as e:
        test_name = request.node.name  # گرفتن نام تست
        save_screenshot(driver, screenshot_base_dir, device_name, udid, test_name)
        pytest.fail(f"Test failed due to error: {e}")

    finally:
        driver.quit()
