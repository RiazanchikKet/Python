from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckOut:

    def __init__(self, driver):
        self.browser = driver

    def check_zip(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#zip-code"))
            )
        zip_code = self.browser.find_element(
            By.CSS_SELECTOR, "#zip-code"
            ).value_of_css_property("background-color")
        return zip_code

    def check_input_fields(self):
        input_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                        "#phone", "#city", "#country", "#job-position",
                        "#company"]
        for input_field in input_fields:
            color = self.browser.find_element(
                By.CSS_SELECTOR, input_field
                ).value_of_css_property("background-color")
        return color
