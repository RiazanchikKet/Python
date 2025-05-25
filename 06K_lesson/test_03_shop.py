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
def test_shop(driver):
    driver.get(
        "https://www.saucedemo.com/"
               )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))
    )

    driver.find_element(
        By.CSS_SELECTOR, "#user-name"
        ).send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.CSS_SELECTOR, "#login-button"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
            )
    )
# добавить в корзину labs-backpack
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
        ).click()

# добавить в корзину labs-bolt-t-shirt
    t_shirt = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        )
    driver.execute_script("arguments[0].scrollIntoView(true);", t_shirt)
    t_shirt.click()

# добавить в корзину labs-onesie
    onsine = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
        )
    driver.execute_script("arguments[0].scrollIntoView(true);", onsine)
    onsine.click()

# перейти в корзину
    driver.find_element(
        By.CSS_SELECTOR, "#remove-sauce-labs-onesie"
    ).send_keys(Keys.HOME)
    shopping_cart = driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container"
    )
    shopping_cart.find_element(By.CSS_SELECTOR, "a").click()

# нажать checkout
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# заполнить форму данными
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ekaterina")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Riazanova")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")

# нажать continue
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

# прочитать итоговую стоимость со страницы (Total)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    total = driver.find_element(
        By.CSS_SELECTOR, "div[data-test='total-label']"
    ).text
    print(f"Стоимость {total}")

# проверить, что Total = 58,29
    assert total == "Total: $58.29"
