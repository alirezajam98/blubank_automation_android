from pages.base_page import BasePage


class CreateAccountOnBoardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Add methods specific to the CreateAccountOnBoardingPage here
