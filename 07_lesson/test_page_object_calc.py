
from selenium import webdriver
from calcClass.ClickDelay import ClickDelay
from calcClass.ClickButtons import ClickButtons
from calcClass.checkout import CheckTablo


def test_calc():
    driver = webdriver.Chrome()

    delay = ClickDelay(driver)
    delay.send_delay(45)

    buttons = ClickButtons(driver)
    buttons.click_seven()
    buttons.click_plus()
    buttons.click_eight()
    buttons.the_equal_button()

    tablo = CheckTablo(driver)
    num = tablo.checkout()

    assert num == '15'

    driver.quit()
