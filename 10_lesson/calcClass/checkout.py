from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckTablo:
    """
    Позволяет вывести значение с табло калькулятора после проведения
    вычислительных операций.
    """
    def __init__(self, driver: str):
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        """
        self.browser = driver

    def checkout(self) -> int:
        """
        Находит на странице табло с результатом вычисления и после ранее
        определенного ожидания (при вызове метода send_delay в класса
        ClickDelay) возвращает числовое значение вычисления
        """
        WebDriverWait(self.browser, 50).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
               )
            )
        tablo = self.browser.find_element(By.CSS_SELECTOR, "div.screen").text
        return tablo
