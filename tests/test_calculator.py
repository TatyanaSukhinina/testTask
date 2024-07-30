from playwright.sync_api import sync_playwright, expect
import pytest

# Параметризованный тест для проверки различных операций калькулятора
# Используем pytest.mark.parametrize для передачи разных наборов входных данных
@pytest.mark.parametrize(
    "operand1, operand2, operation, expected_result",
    [
        # Тестовые случаи для разных операций
        (5, 3, "+", 8),   # Сложение
        (10, 4, "-", 6),  # Вычитание
        (7, 2, "*", 14),  # Умножение
        (12, 3, "/", 4),  # Деление
        # Тестовые случаи для проверки ошибок
        (10, 0, "/", "Ошибка: Деление на ноль"), # Деление на ноль
        ("abc", 5, "+", "Ошибка: Некорректный ввод"), # Некорректный ввод
        ("", 5, "+", "Ошибка: Некорректный ввод"), # Пустое поле
        # Тестовые случаи для проверки граничных условий
        (1000000, 500000, "+", 1500000), # Большие числа
        (-5, 3, "+", -2), # Отрицательные числа
    ]
)
def test_calculator_operations(calculator_page, operand1, operand2, operation, expected_result):
    '''Параметризованный тест для проверки различных операций калькулятора'''
    # Устанавливаем значения операндов
    calculator_page.set_operand1(operand1)
    calculator_page.set_operand2(operand2)
    # Выбираем операцию
    calculator_page.select_operation(operation)
    # Кликаем на кнопку "Вычислить"
    calculator_page.click_calculate()

    # Проверяем результат
    if isinstance(expected_result, str):
        # Если ожидается строка (ошибка), то проверяем текст
        expect(calculator_page.result_paragraph).to_have_text(expected_result)
    else:
        # Иначе ожидается число, проверяем результат
        calculator_page.expect_result(expected_result)

# Запускаем тесты с помощью pytest
with sync_playwright() as playwright:
    pytest.main(["-v", "-s"])
