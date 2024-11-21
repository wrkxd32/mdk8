class Calculation:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль запрещено")
        return a / b