from playwright.sync_api import sync_playwright, expect
import pytest
import random


def generate_random_operands(max_value=10000):
    return random.randint(1, max_value), random.randint(1, max_value)


@pytest.mark.parametrize(
    "operation",
    [
        "+",
        "-",
        "*",
        "/"
    ]
)
def test_basic_calculation(calculator_page, operation):
    """Тест для проверки основных операций с целыми числами"""
    operand1, operand2 = generate_random_operands()
    calculator_page.set_operand1(operand1)
    calculator_page.set_operand2(operand2)
    calculator_page.select_operation(operation)
    calculator_page.click_calculate()
    expected_result = eval(f"{operand1} {operation} {operand2}")
    assert calculator_page.get_result_text() == str(expected_result)


@pytest.mark.parametrize(
    "operation",
    [
        "+",
        "-",
        "*",
        "/"
    ]
)
def test_calculation_with_float(calculator_page, operation):
    """Тест для проверки операций с дробными числами"""
    operand1, operand2 = generate_random_operands(max_value=1000)
    operand1 /= 10
    operand2 /= 10
    calculator_page.set_operand1(operand1)
    calculator_page.set_operand2(operand2)
    calculator_page.select_operation(operation)
    calculator_page.click_calculate()
    expected_result = eval(f"{operand1} {operation} {operand2}")
    assert calculator_page.get_result_text() == str(expected_result)


def test_division_on_zero(calculator_page):
    """Тест для проверки деления на ноль"""
    operand1 = 10
    operand2 = 0
    calculator_page.set_operand1(operand1)
    calculator_page.set_operand2(operand2)
    calculator_page.select_operation("/")
    calculator_page.click_calculate()
    assert "Ошибка: Деление на ноль" in calculator_page.get_result_text()

# Запускаем тесты с помощью pytest
with sync_playwright() as playwright:
    pytest.main(["-v", "-s"])
