class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, a, b):
        self.value = a + b

    def subtract(self, a, b):
        self.value = a - b

    def multiply(self, a, b):
        self.value = a * b

    def divide(self, a, b):
        if b == 0:
            self.value = "No se puede dividir por cero"
        else:
            self.value = a / b
