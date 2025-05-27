from selenium.webdriver.common.by import By


class ClickButtons:

    def __init__(self, driver):
        self.browser = driver

    def click_seven(self):
        self.browser.find_element(By.XPATH, "//*[text()='7']").click()

    def click_plus(self):
        self.browser.find_element(By.XPATH, "//*[text()='+']").click()

    def click_eight(self):
        self.browser.find_element(By.XPATH, "//*[text()='8']").click()

    def the_equal_button(self):
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
            )
        self.browser.find_element(By.XPATH, "//*[text()='=']").click()
