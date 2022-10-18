# This is an original Python script.
x = int(input('Введите n '))


def fibonacci(n):
    if n >= 2:
        n = fibonacci(n-1) + fibonacci(n-2)
    elif n <= -2:
        n = fibonacci(n+1) + fibonacci(n+2)
    return n


print(fibonacci(x))

# (C) Voynov Daniil
