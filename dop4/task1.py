def wrap(number):
    number = list(number[::-1])

    print(*number, sep=',', end='')
    print('; кількість символів = ' + str(len(number)))


number = str(input('Введіть число: '))

wrap(number)