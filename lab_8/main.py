def square(number):
    return number ** 2

print(square(4))
print()

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))
print()

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
print()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))