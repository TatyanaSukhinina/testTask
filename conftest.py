import pytest
from calculator_page import CalculatorPage
import playwright
from playwright.sync_api import sync_playwright, expect

# Фикстура, которая создает экземпляр CalculatorPage перед каждым тестом
# и уничтожает его после завершения теста
@pytest.fixture
def calculator_page():
    with sync_playwright() as playwright:  # Получаем Playwright
        browser = playwright.chromium.launch(headless=False)  # headless=False для визуального наблюдения
        page = browser.new_page()
<<<<<<< HEAD
        page.goto("file:///path/to/calculator.html")  #путь HTML-файлу
=======
        page.goto("file:///path/to/your/calculator.html")  #путь HTML-файлу
>>>>>>> 20faf09dda396df69f933cc8ef1cbe4c1d91b9db
        yield CalculatorPage(page)  # Возвращаем экземпляр CalculatorPage
        browser.close()