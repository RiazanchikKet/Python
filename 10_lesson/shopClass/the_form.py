from selenium.webdriver.common.by import By
import allure


class TheForm:
    """
    Из корзины переходит на страницу заполнения даных для совершения покупки.
    """

    def __init__(self, driver: str):
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        """
        self.browser = driver

    @allure.step("Ввести значение {term} в поле \"First Name\"")
    def first_name(self, term: str) -> None:
        """
        Находит на странице элемент "First Name" и передает строковое значение.

        Параметры:
        term - принимает строковое значение на вход при вызове метода.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#first-name"
            ).send_keys(term)

    @allure.step("Ввести значение {term} в поле \"Last Name\"")
    def last_name(self, term: str) -> None:
        """
        Находит на странице элемент "Last Name" и передает строковое значение.

        Параметры:
        term - принимает строковое значение на вход при вызове метода.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#last-name"
            ).send_keys(term)

    @allure.step("Ввести значение {term} в поле \"Zip/Postal Code\"")
    def postal_code(self, term: int) -> None:
        """
        Находит на странице элемент "Zip/Postal Code" и передает числовое
        значение.

        Параметры:
        term - принимает числовое значение на вход при вызове метода.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#postal-code"
            ).send_keys(term)

    @allure.step("нажать на кнопку Continue")
    def click_continue(self) -> None:
        """
        Находит на странице кнопку "Continue" и нажимает на нее.
        """
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()
