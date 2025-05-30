import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures
def test_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
               )

    driver.find_element(
        By.CSS_SELECTOR, "input[name='first-name']"
        ).send_keys("Иван")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='last-name']"
        ).send_keys("Петров")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='address']"
        ).send_keys("Ленина, 55-3")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']"
        ).send_keys("test@skypro.com")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']"
        ).send_keys("+7985899998787")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='city']"
        ).send_keys("Москва")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='country']"
        ).send_keys("Россия")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='job-position']"
        ).send_keys("QA")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='company']"
        ).send_keys("SkyPro")

    submit = driver.find_element(By.CSS_SELECTOR, "div button[type='submit']")
    submit.send_keys(Keys.END)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div button[type='submit']")
            )
        )
    submit.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#zip-code"))
        )
    zip_code = driver.find_element(
        By.CSS_SELECTOR, "#zip-code"
        ).value_of_css_property("background-color")
    assert zip_code == "rgba(248, 215, 218, 1)"

    input_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                    "#phone", "#city", "#country", "#job-position", "#company"]
    for input_field in input_fields:
        color = driver.find_element(
            By.CSS_SELECTOR, input_field
            ).value_of_css_property("background-color")
    assert color == "rgba(209, 231, 221, 1)"
