from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoCart:

    def __init__(self, driver):
        self.browser = driver

    def go_over_to_cart(self):
        self.browser.find_element(
            By.CSS_SELECTOR, "#remove-sauce-labs-onesie"
            ).send_keys(Keys.HOME)

        shopping_cart = self.browser.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container"
            )
        shopping_cart.find_element(By.CSS_SELECTOR, "a").click()

    def click_checkout(self):
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
            )
        self.browser.find_element(By.CSS_SELECTOR, "#checkout").click()
