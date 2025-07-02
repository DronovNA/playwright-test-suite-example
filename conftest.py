import pytest
from playwright.sync_api import sync_playwright
import allure
import os
from dotenv import load_dotenv

load_dotenv()

def pytest_addoption(parser):
    """Добавляем опцию для выбора браузера"""
    parser.addoption(
        "--browser", action="store", default="chromium", choices=["chromium", "firefox", "webkit"],
        help="Выберите браузер для тестов"
    )

@pytest.fixture(scope="session")
def browser(request):
    """Запускаем выбранный браузер"""
    browser_name = request.config.getoption("--browser")
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    """Создаем контекст для браузера"""
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    """Создаем страницу для каждого теста"""
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def base_url():
    """Базовый URL для тестов"""
    url = os.getenv("BASE_URL")
    if not url:
        raise ValueError("BASE_URL environment variable is not set.")
    return url

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Хук для добавления аттачей в отчёт Allure при неудаче"""
    outcome = call.excinfo
    if outcome is not None:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
