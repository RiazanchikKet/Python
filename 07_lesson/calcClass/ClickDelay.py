from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


class ClickDelay:

    def __init__(self, driver):
        self.browser = driver
        self.browser.get(link)
        self.browser.maximize_window()

    def send_delay(self, term):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
            )
        delay = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(int(term))
