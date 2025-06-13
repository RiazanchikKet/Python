from company_table import CompanyTable
import pytest
from config import URL_db


db = CompanyTable(URL_db)


@pytest.fixture(scope='session')
def area():
    use_db = {}
    use_db.clear()
    yield db
    use_db.clear()


@pytest.mark.usefixtures
def test_add_entity():
    user_id = "12345"
    level = "Intermediate"
    education_form = "group"
    subject_id = "1"
    db.add_student(user_id, level, education_form, subject_id)
    students = db.check_by_id(user_id)

    for student in students:
        assert student['user_id'] == int(user_id)


@pytest.mark.usefixtures
def test_edit_entity():
    user_id = "12345"
    level = "Uper-Mediate"
    education_form = "group"
    subject_id = "1"
    where_id = "12345"
    db.edit_student(user_id, level, education_form, subject_id, where_id)
    students = db.check_by_id(user_id)

    for student in students:
        assert student['level'] == level


@pytest.mark.usefixtures
def test_delete_entity():
    user_id = "12345"
    db.delete_student(user_id)
    students = db.check_by_id(user_id)

    assert students == []
