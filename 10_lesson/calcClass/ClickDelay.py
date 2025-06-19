from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

link = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


class ClickDelay:
    """
    Позволяет найти и взаимодействовать с элементом на странице, обозначающее
    время в секундах, через которое можно получить результат вычисления на
    калькуляторе.
    """

    def __init__(self, driver):
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        link - ссылка, по которой переходит WebDriver для выполнения тестов.
        """
        self.browser = driver
        self.browser.get(link)
        self.browser.maximize_window()

    @allure.step("Ввести {term} в окне \"ожидает '5' секунд\"")
    def send_delay(self, term: int) -> None:
        """
        Находит на странице табло, принимающее на вход числовое значение,
        указанное на входе при вызове метода. Это значение показывает через
        сколько секунд будет получен результат после нажатия на кнопку "=".

        Параметры:
        term - целое числовое значение, которое на вход принимает метод.
        """
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
            )
        delay = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(term)
