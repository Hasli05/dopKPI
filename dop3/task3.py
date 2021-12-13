def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input('Введіть число: '))

print('Число Фібоначчі: ', fibonacci(number))