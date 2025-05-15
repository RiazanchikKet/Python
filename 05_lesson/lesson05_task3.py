from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
search = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search.send_keys("Sky")
search.clear()
search.send_keys("Pro")


driver.quit()
