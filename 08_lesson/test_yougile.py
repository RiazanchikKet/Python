from YouGile import YouGile
import pytest


api = YouGile("https://ru.yougile.com")
api_key = "HDPVQ0hSN4itqbZWISFAurXcI76ODsRK5W9eZwooQmOhP+fDRNYXm4xTndNp9gnz"


# вспомогательные методы
def get_id_company():
    login = 'katyunchik46@gmail.com'
    password = 'QNrz,A9._ix3$s,'
    name = 'Тестовая'
    id_company = api.get_id_company(login, password, name)
    return id_company


def get_api_key():
    login = 'katyunchik46@gmail.com'
    password = 'QNrz,A9._ix3$s,'
    id_company = get_id_company()
    api_key = api.get_API_key(login, password, id_company)
    return api_key


# Выполнить 3 метода:
# 1. Создать проект
# позитивный тест
@pytest.mark.create_project
@pytest.mark.positive_test
def test_positive_create_project():
    # api_key = get_api_key()
    title = 'Skypro'
    project = api.create_project(title, api_key)
    result = project['id']
    get_project = api.get_list_projects_id(result, api_key)

    assert get_project['id'] == project['id']
    assert get_project['title'] == title


# негативный тест
@pytest.mark.create_project
@pytest.mark.negative_test
def test_negative_create_project():
    # api_key = get_api_key()
    title = ''
    project = api.create_project(title, api_key)

    assert project['message'][0] == 'title should not be empty'


# 2. Изменить проект
# позитивный тест
@pytest.mark.edit_project
@pytest.mark.positive_test
def test_positive_edit_project():
    # api_key = get_api_key()
    title = 'New project'
    deleted = False
    get_project = api.get_list_projects(
        api_key, params_to_add={'title': 'Skypro'}
        )
    id = get_project['content'][0]['id']
    edit_project = api.edit_project(id, title, deleted, api_key)
    id_new = edit_project['id']
    get_project_id = api.get_list_projects_id(id_new, api_key)

    assert get_project_id['title'] == title
    assert edit_project['id'] == get_project_id['id']


# негативный тест
@pytest.mark.edit_project
@pytest.mark.negative_test
def test_negative_edit_project():
    # api_key = get_api_key()
    title = 'New project'
    deleted = False
    id = None
    edit_project = api.edit_project(id, title, deleted, api_key)

    assert edit_project['message'] == 'Проект не найден'


# 3. Получить по id
# позитивный тест
@pytest.mark.get_list_project
@pytest.mark.positive_test
def test_positive_get_project():
    # api_key = get_api_key()
    get_project = api.get_list_projects(
        api_key, params_to_add={'title': 'New project'}
        )
    id = get_project['content'][0]['id']
    get_project_id = api.get_list_projects_id(id, api_key)

    assert get_project_id['title'] == 'New project'
    assert get_project_id['id'] == id


# негативный тест
@pytest.mark.get_list_project
@pytest.mark.negative_test
def test_negative_get_project():
    api_key = 'Bearer '
    get_project = api.get_list_projects(
        api_key, params_to_add={'title': 'New project'}
        )
    id = get_project
    get_project_id = api.get_list_projects_id(id, api_key)

    assert get_project_id['statusCode'] == 401
    assert get_project_id['message'] == 'Unauthorized'
