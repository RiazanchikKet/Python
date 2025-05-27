import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures
def test_calc(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
               )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
    )

    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")

    # нажать на кнопку 7
    driver.find_element(By.XPATH, "//*[text()='7']").click()

    # нажать на кнопку  +
    driver.find_element(By.XPATH, "//*[text()='+']").click()

    # нажать на кнопку  8
    driver.find_element(By.XPATH, "//*[text()='8']").click()

    # нажать на кнопку =
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, "//*[text()='=']").click()

    # проверить результат (равен 15)
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"), "15"
            )
    )

    tablo = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert tablo == "15"
