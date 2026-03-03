try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

print()

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")

print()

class Shape:
    def area(self):
        raise NotImplementedError('Subclasses must implement area method')

class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot compute the square root of a negative number.")
    return number ** 0.5

try:
    result = square_root(-9)
except NegativeNumberError as e:
    print(f"Error: {e}")

print()

class ApplicationError(Exception):
    pass

class DatabaseError(ApplicationError):
    pass

class ValidationError(ApplicationError):
    pass

try:
    raise ValidationError("Invalid input data")
except ValidationError as e:
    print(f"Validation error: {e}")
except ApplicationError as e:
    print(f"Application error: {e}")

print()

def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    return a / b

print(divide(10, 0))
