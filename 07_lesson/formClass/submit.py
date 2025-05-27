from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClickSubmit:

    def __init__(self, driver):
        self.browser = driver

    def clicl_submit(self):
        submit = self.browser.find_element(
            By.CSS_SELECTOR, "div button[type='submit']"
            )
        submit.send_keys(Keys.END)

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div button[type='submit']")
                )
            )
        submit.click()
