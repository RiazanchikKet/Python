from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class GoCart:
    """
    Позволяет перейти в корзину и просмотреть выбранный товар, а также
    продолжить покупку.
    """

    def __init__(self, driver: str):
        """
        Конструктор, позволяющий с помощью вебдрайвера открыть браузер
        и выполнить тестовые сценарии.

        Параметры:
        driver - значение (WebDriver), которое принимает класс.
        """
        self.browser = driver

    @allure.step("Перейти в корзину, нажав на ее значок в верхнем правом углу\
                 страницы")
    def go_over_to_cart(self) -> None:
        """
        Находит на странице кнопку для перехода в корзину и нажимает ее.
        """
        self.browser.find_element(
            By.CSS_SELECTOR, "#remove-sauce-labs-onesie"
            ).send_keys(Keys.HOME)

        shopping_cart = self.browser.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container"
            )
        shopping_cart.find_element(By.CSS_SELECTOR, "a").click()

    @allure.step("Нажать на кнопку Checkout")
    def click_checkout(self):
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)"
            )
        self.browser.find_element(By.CSS_SELECTOR, "#checkout").click()
