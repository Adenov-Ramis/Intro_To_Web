PI = 3.14159

a = 10
b = 15
c = (a + b) // (b - a) * 10
d = 5
c, d = d, c
print(c * c * PI)

name = input("Enter your name: ")
age = int(input('Enter your age: '))
print(f'Your name is {name} and your age is {age} years old')

n = int(input('Enter n: '))
m = int(input('Enter m: '))
k = int(input('Enter k: '))

print(f'Sum: {n + m + k}')
print(f'Average: {(n + m + k) / 3}')
print(f'Product: {n * m * k}')