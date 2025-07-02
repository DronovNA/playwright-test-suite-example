import pytest
import allure
from page_objects.example_page import ExamplePage

@pytest.mark.parametrize("url", ["https://example.com", "https://example.org"])
@allure.feature('Главная страница')
@allure.story('Проверка заголовка страницы')
def test_page_title(url, page, base_url):
    example_page = ExamplePage(page, base_url)
    example_page.open()
    page.goto(url)
    title = page.title()
    allure.attach(title, name="Page Title", attachment_type=allure.attachment_type.TEXT)
    assert title == "Example Domain", f"Expected title 'Example Domain', but got {title}"

@allure.feature('Форма')
@allure.story('Заполнение текстового поля')
def test_input_field(page, base_url):
    example_page = ExamplePage(page, base_url)
    example_page.open()
    example_page.fill_input("input[name='q']", "Playwright")
    input_value = page.locator("input[name='q']").input_value()
    allure.attach(input_value, name="Input Value", attachment_type=allure.attachment_type.TEXT)
    assert input_value == "Playwright"

@allure.feature('Форма')
@allure.story('Отправка формы')
def test_form_submission(page, base_url):
    example_page = ExamplePage(page, base_url)
    example_page.open()
    example_page.fill_input("input[name='q']", "Test")
    example_page.submit_form("button[type='submit']")
    assert page.url == "https://example.com/search?q=Test"  # Меняй под свою логику

@allure.feature('Текст на странице')
@allure.story('Проверка текста на главной странице')
def test_text_on_page(page, base_url):
    example_page = ExamplePage(page, base_url)
    example_page.open()
    text = example_page.get_text("h1")
    allure.attach(text, name="Page Text", attachment_type=allure.attachment_type.TEXT)
    assert text == "Example Domain", f"Expected text 'Example Domain', but got {text}"

@allure.feature('Навигация')
@allure.story('Переход по ссылкам')
def test_navigation(page, base_url):
    example_page = ExamplePage(page, base_url)
    example_page.open()
    page.click("a")  # Переходим по ссылке
    assert page.url == "https://www.iana.org/domains/example"
