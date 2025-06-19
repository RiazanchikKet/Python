from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AddCart:
    """
    Позволяет выбирать и добавлять в корзину вещи на странице после
    прохождения авторизации.
    """

    def __init__(self, driver: str):
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        """
        self.browser = driver

    @allure.step("Подождать прогрузки страницы до видимости элемента\
                 labs-backpack")
    def add_cart(self) -> None:
        """
        Ожидает прогрузки странице и находит элемент labs-backpack.
        """
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
                )
            )

    @allure.step("Добавить в корзину элемент labs-backpack")
    def labs_backpack(self) -> None:
        """
        Добавляет в корзину элемент labs-backpack.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
            ).click()

    @allure.step("Добавить в корзину элемент labs-bolt-t-shirt")
    def labs_bolt_t_shirt(self) -> None:
        """
        Находит на странице и добавляет в корзину элемент labs-bolt-t-shirt.
        """
        t_shirt = self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
            )
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", t_shirt
            )
        t_shirt.click()

    @allure.step("Добавить в корзину элемент labs-onesie")
    def labs_onesie(self) -> None:
        """
        Находит на странице и добавляет в корзину элемент labs-onesie.
        """
        onsine = self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
            )
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", onsine
            )
        onsine.click()
