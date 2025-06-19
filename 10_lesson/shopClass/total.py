from selenium.webdriver.common.by import By
import allure


class CheckTotal:
    """
    После внесения данных для совершения покупки открывается страница, где
    отображен выбранный товар, его стоимость отдельно и общая стоимость.
    """

    def __init__(self, driver: str):
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        """
        self.browser = driver

    @allure.step("Найти на странице Price Total")
    def check_total(self) -> int:
        """
        Находит на странице элемент "Price Total" и возвращает его числовое
        значение.
        """
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
            )
        total = self.browser.find_element(
            By.CSS_SELECTOR, "div[data-test='total-label']"
        ).text
        return total
