
from selenium import webdriver
from calcClass.ClickDelay import ClickDelay
from calcClass.ClickButtons import ClickButtons
from calcClass.checkout import CheckTablo
import allure


@allure.title("E2E. Калькулятор")
@allure.description("Открыть сайт, задать время ожидания получения результата,\
                    произвести вычисление, дождаться и сравнить результат,\
                    появившийся на табло с тем, который должен получиться.")
@allure.feature("Проверка логики вычисления калькулятора.")
@allure.severity("BLOCKER")
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

    print(f"7 + 8 = {num}")

    with allure.step("Сравнить результат вычисления калькулятора 7+8, которое\
                     отображается на его табло."):
        assert num == '15'

    driver.quit()
