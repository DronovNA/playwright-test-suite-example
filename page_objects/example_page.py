import allure
from playwright.sync_api import Page

class ExamplePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = base_url  # Используем URL, переданный через фикстуру

    @allure.step("Открываем страницу {self.url}")
    def open(self):
        """Открываем страницу"""
        self.page.goto(self.url)

    @allure.step("Получаем заголовок страницы")
    def get_title(self):
        """Получаем заголовок страницы"""
        return self.page.title()

    @allure.step("Заполняем поле {selector} значением {value}")
    def fill_input(self, selector: str, value: str):
        """Заполняем текстовое поле"""
        self.page.fill(selector, value)

    @allure.step("Отправляем форму через кнопку {selector}")
    def submit_form(self, selector: str):
        """Отправляем форму"""
        self.page.click(selector)

    @allure.step("Получаем текст элемента {selector}")
    def get_text(self, selector: str):
        """Получаем текст из элемента"""
        return self.page.inner_text(selector)

    @allure.step("Проверка видимости элемента {selector}")
    def is_visible(self, selector: str):
        """Проверяем, что элемент видим"""
        return self.page.is_visible(selector)
