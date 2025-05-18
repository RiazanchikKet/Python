from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
user_name = driver.find_element(By.CSS_SELECTOR, "#username")
user_name.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()

text_succes = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(text_succes)

driver.quit()
