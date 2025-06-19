from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Authorization:
    """
    Позволяет пройти авторизацию на странице по ссылке, указанной в
    контрукторе класса.
    """

    def __init__(self, driver: str):
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        """
        self.browser = driver
        self.browser.get(
            "https://www.saucedemo.com/"
            )
        self.browser.maximize_window()

    @allure.step("Ввести значение {term} в поле \"Username\"")
    def user_name(self, term: str) -> None:
        """
        Находит на странице элемент username и передает строковое значение,
        переданное на входе при вызове метода.

        Параметры:
        term - принимает на вход строковое значение.
        """
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name"))
                )
        self.browser.find_element(
            By.CSS_SELECTOR, "#user-name"
            ).send_keys(term)

    @allure.step("Ввести значение {term} в поле \"Password\"")
    def password(self, term: str) -> None:
        """
        Находит на странице элемент password и передает строковое значение,
        переданное на входе при вызове метода.

        Параметры:
        term - принимает на вход строковое значение.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#password"
            ).send_keys(term)

    @allure.step("Нажать на кнопку Login")
    def click_login(self) -> None:
        """
        Находит на странице и нажимает на кнопку "login".
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#login-button"
            ).click()
