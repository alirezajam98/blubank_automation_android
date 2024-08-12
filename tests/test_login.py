import time

import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.HomePage import HomePage
from pages.Login.Login_page import LoginPage


def test_login_with_biometric(create_driver_fixture):
    driver = create_driver_fixture

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

    except (NoSuchElementException, TimeoutException) as e:
        # در صورت بروز خطا، اسکرین‌شات بگیرید و خطا را ثبت کنید
        driver.save_screenshot(f"screenshot_{int(time.time())}.png")
        pytest.fail(f"Test failed due to error: {e}")

    finally:
        driver.quit()
