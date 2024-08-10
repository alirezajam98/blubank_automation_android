from telnetlib import EC

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from pages.Login.Login_page import LoginPage
from pages.base_page import BasePage
from pages.KYC.create_account_onboarding_page import CreateAccountOnBoardingPage

class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.open_account_button = (MobileBy.ID, "com.samanpr.blu.dev:id/openAccountButton")
        self.has_account_button = (MobileBy.ID, "com.samanpr.blu.dev:id/hasAccountButton")

    def get_open_account_button_title(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.open_account_button)
        )
        return element.get_attribute("text")

    def get_has_account_button_title(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.has_account_button)
        )
        return element.get_attribute("text")

    def click_open_account_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.open_account_button)
        )
        element.click()
        return CreateAccountOnBoardingPage(self.driver)

    def click_has_account_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.has_account_button)
        )
        element.click()
        return LoginPage(self.driver)
