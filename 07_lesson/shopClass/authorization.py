from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Authorization:

    def __init__(self, driver):
        self.browser = driver
        self.browser.get(
            "https://www.saucedemo.com/"
            )
        self.browser.maximize_window()

    def user_name(self, term):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))
                )
        self.browser.find_element(
            By.CSS_SELECTOR, "#user-name"
            ).send_keys(term)

    def password(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "#password"
            ).send_keys(term)

    def click_login(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#login-button"
            ).click()
