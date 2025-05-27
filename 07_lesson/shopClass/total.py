from selenium.webdriver.common.by import By


class CheckTotal:

    def __init__(self, driver):
        self.browser = driver

    def check_total(self):
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
            )
        total = self.browser.find_element(
            By.CSS_SELECTOR, "div[data-test='total-label']"
        ).text
        return total
