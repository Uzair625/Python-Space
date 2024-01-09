class MyInteger:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("Input must be an integer.")
        self.value = value

    def display(self):
        print(f"The integer value is: {self.value}")

    def add(self, other):
        if not isinstance(other, MyInteger):
            raise ValueError("Operand must be an instance of MyInteger.")
        result = self.value + other.value
        return MyInteger(result)

    def subtract(self, other):
        if not isinstance(other, MyInteger):
            raise ValueError("Operand must be an instance of MyInteger.")
        result = self.value - other.value
        return MyInteger(result)

    def multiply(self, other):
        if not isinstance(other, MyInteger):
            raise ValueError("Operand must be an instance of MyInteger.")
        result = self.value * other.value
        return MyInteger(result)

# Example usage
num1 = MyInteger(5)
num2 = MyInteger(3)

num1.display()
num2.display()

sum_result = num1.add(num2)
sum_result.display()

difference_result = num1.subtract(num2)
difference_result.display()

product_result = num1.multiply(num2)
product_result.display()
