def arabicInRoman(number):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += number // arabic * roman
        number %= arabic
    return result


status = True

while status:
    number = int(input("Введіть число яке хочете перевисти в римське: "))
    arabicInRoman(number)

    a = str(input('Бажаєте продовжити? (y - так,n - ні)'))

    if a == 'y':
        status = True
        continue
    elif a == 'n':
        status = False
        break
    else:
        print(0)