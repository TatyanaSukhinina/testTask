from playwright.sync_api import Page, expect

class CalculatorPage:
    def __init__(self, page: Page):
        self.page = page

        # Локаторы элементов
        self.operand1_input = page.locator("#operand1")
        self.operand2_input = page.locator("#operand2")
        self.operation_select = page.locator("#operation")
        self.calculate_button = page.locator("#calculate")
        self.result_paragraph = page.locator("#result")

    def set_operand1(self, value: int):
        self.operand1_input.fill(str(value))

    def set_operand2(self, value: int):
        self.operand2_input.fill(str(value))

    def select_operation(self, operation: str):
        self.operation_select.select_option(value=operation)

    def click_calculate(self):
        self.calculate_button.click()

    def get_result(self):
        return self.result_paragraph.inner_text()

    def expect_result(self, expected_result: int):
        expect(self.result_paragraph).to_have_text(str(expected_result))