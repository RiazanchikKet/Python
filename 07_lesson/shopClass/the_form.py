from selenium.webdriver.common.by import By


class TheForm:

    def __init__(self, driver):
        self.browser = driver

    def first_name(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "#first-name"
            ).send_keys(term)

    def last_name(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "#last-name"
            ).send_keys(term)

    def postal_code(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "#postal-code"
            ).send_keys(term)

    def click_continue(self):
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()
