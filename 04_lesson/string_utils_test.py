import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_text, expected_text',
                         [("hello", "Hello"), ("HELLO", "Hello"),
                          ("!hello.", "!hello."),
                          (" при вет ", " при вет "),
                          ("123456", "123456")])
def test_capitalize_positive(input_text, expected_text):
    assert string_utils.capitalize(input_text) == expected_text


@pytest.mark.positive
@pytest.mark.parametrize('input_text, expected_text', [
    ("    Hello ", "Hello "),
    ("Hello 123", "Hello 123")])
def test_trim_positive(input_text, expected_text):
    assert string_utils.trim(input_text) == expected_text


@pytest.mark.positive
@pytest.mark.parametrize('input_text, input_symbol, expected_res',
                         [("Hello", "H", True), ("Hello", "A", False),
                          ("При вет", " ", True), ("Hello!", "!", True),
                          ("123456", "456", True)])
def test_contains_positive(input_text, input_symbol, expected_res):
    assert string_utils.contains(input_text, input_symbol) == expected_res


@pytest.mark.positive
@pytest.mark.parametrize('input_text, input_symbol, expected_res',
                         [("Hello", "l", "Heo"),
                          ("Hello World", "World", "Hello "),
                          ("! Hello World !", " ", "!HelloWorld!"),
                          ("Hello", "123", "Hello")])
def test_delete_sibmol_positive(input_text, input_symbol, expected_res):
    assert string_utils.delete_symbol(input_text, input_symbol) == expected_res


# негативные автотесты
@pytest.mark.negative
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('input_text, expected_text',
                         [("Hello", "hello"), ("1hello", "1Hello"),
                          (" ", " "), ("", "")])
def test_capitalize_negative(input_text, expected_text):
    assert string_utils.capitalize(input_text) == expected_text


@pytest.mark.negative
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('input_text, expected_text',
                         [(" Hello World !", "HelloWorld!"),
                          ("Hello ", "Hello"), (" ", ""), ("", "")])
def test_trim_negative(input_text, expected_text):
    assert string_utils.trim(input_text) == expected_text


@pytest.mark.negative
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('input_text, input_symbol, expected_res',
                         [("Hello", "h", False), ("", " ", True),
                          ("Привет", "", False)])
def test_contains_negative(input_text, input_symbol, expected_res):
    assert string_utils.contains(input_text, input_symbol) == expected_res


@pytest.mark.negative
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('input_text, input_symbol, expected_res',
                         [("Hello", "E", "Hello"),
                          ("One = 1", "n 1", "Oe="),
                          ("Hello", "123", "Hello")])
def test_delete_sibmol_negative(input_text, input_symbol, expected_res):
    assert string_utils.delete_symbol(input_text, input_symbol) == expected_res
