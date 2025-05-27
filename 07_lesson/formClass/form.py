from selenium.webdriver.common.by import By


class FormName:

    def __init__(self, driver):
        self.browser = driver
        self.browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        self.browser.maximize_window()

    def first_name(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='first-name']"
            ).send_keys(term)

    def last_name(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='last-name']"
            ).send_keys(term)

    def address(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='address']"
            ).send_keys(term)

    def e_mail(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='e-mail']"
            ).send_keys(term)

    def phone(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='phone']"
            ).send_keys(term)

    def city(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='city']"
            ).send_keys(term)

    def country(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='country']"
            ).send_keys(term)

    def job_position(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='job-position']"
            ).send_keys(term)

    def company(self, term):
        self.browser.find_element(
            By.CSS_SELECTOR, "input[name='company']"
            ).send_keys(term)
