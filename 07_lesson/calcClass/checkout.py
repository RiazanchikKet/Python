from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckTablo:

    def __init__(self, driver):
        self.browser = driver

    def checkout(self):
        # проверить результат (равен 15)
        WebDriverWait(self.browser, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
               )
            )
        tablo = self.browser.find_element(By.CSS_SELECTOR, "div.screen").text
        return tablo
