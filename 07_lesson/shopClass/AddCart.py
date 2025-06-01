from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCart:

    def __init__(self, driver):
        self.browser = driver

    def add_cart(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
                )
            )

    def labs_backpack(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
            ).click()

    def labs_bolt_t_shirt(self):
        t_shirt = self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
            )
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", t_shirt
            )
        t_shirt.click()

    def labs_onesie(self):
        onsine = self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
            )
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", onsine
            )
        onsine.click()
