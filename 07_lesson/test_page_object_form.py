
from selenium import webdriver
from formClass.form import FormName
from formClass.submit import ClickSubmit
from formClass.check import CheckOut


def test_form():
    driver = webdriver.Chrome()

    personal_data = FormName(driver)
    personal_data.first_name("Иван")
    personal_data.last_name("Петров")
    personal_data.address("Ленина, 55-3")
    personal_data.e_mail("test@skypro.com")
    personal_data.phone("+7985899998787")
    personal_data.city("Москва")
    personal_data.country("Россия")
    personal_data.job_position("QA")
    personal_data.company("SkyPro")

    button = ClickSubmit(driver)
    button.clicl_submit()

    inputs = CheckOut(driver)
    red = inputs.check_zip()
    green = inputs.check_input_fields()

    assert red == "rgba(248, 215, 218, 1)"

    assert green == "rgba(209, 231, 221, 1)"

    driver.quit()
