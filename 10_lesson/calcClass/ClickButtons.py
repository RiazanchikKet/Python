from selenium.webdriver.common.by import By
import allure


class ClickButtons:
    """
    Позволяет находить на странице и нажимать на кнопки калькулятора.
    """

    def __init__(self, driver: str):
        self.browser = driver
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        """

    @allure.step("Нажать на кнопку \"7\"")
    def click_seven(self) -> None:
        """
        Находит на странице и нажимает на кнопку "7"
        """
        self.browser.find_element(By.XPATH, "//*[text()='7']").click()

    @allure.step("Нажать на кнопку \"+\"")
    def click_plus(self) -> None:
        """
        Находит на странице и нажимает на кнопку "+"
        """
        self.browser.find_element(By.XPATH, "//*[text()='+']").click()

    @allure.step("Нажать на кнопку \"8\"")
    def click_eight(self) -> None:
        """
        Находит на странице и нажимает на кнопку "8"
        """
        self.browser.find_element(By.XPATH, "//*[text()='8']").click()

    @allure.step("Нажать на кнопку \"=\"")
    def the_equal_button(self) -> None:
        """
        Находит на странице и нажимает на кнопку "="
        """
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
            )
        self.browser.find_element(By.XPATH, "//*[text()='=']").click()
