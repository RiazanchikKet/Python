from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput?")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

WebDriverWait(driver, 4).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#updatingButton"), "SkyPro"
        )
)
print(button.text)

driver.quit()
