def naturalDivider(number):
    Ans = []
    divider = 2
    while divider * divider <= number:
        if number % divider == 0:
            Ans.append(divider)
            number //= divider
        else:
            divider += 1
    if number > 1:
        Ans.append(number)
    return Ans


number = int(input('Введіть число: '))

arr = naturalDivider(number)
tempArr = []

print('Натуральные сомножители числа', number, ': ')
print(*arr, sep=' * ')

#1