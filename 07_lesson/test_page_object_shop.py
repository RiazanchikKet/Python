
from selenium import webdriver
from shopClass.authorization import Authorization
from shopClass.AddCart import AddCart
from shopClass.GoCart import GoCart
from shopClass.the_form import TheForm
from shopClass.total import CheckTotal


def test_shop():
    driver = webdriver.Chrome()

    auth = Authorization(driver)
    auth.user_name("standard_user")
    auth.password("secret_sauce")
    auth.click_login()

    add_to_cart = AddCart(driver)
    add_to_cart.labs_backpack()
    add_to_cart.labs_bolt_t_shirt()
    add_to_cart.labs_onesie()

    go = GoCart(driver)
    go.go_over_to_cart()
    go.click_checkout()

    form = TheForm(driver)
    form.first_name("Ekaterina")
    form.last_name("Riazanova")
    form.postal_code("123456")
    form.click_continue()

    num = CheckTotal(driver)
    total = num.check_total()

    print(f"Стоимость - ${total}")

    assert total == "Total: $58.29"
    driver.quit()
