status = True

while status:
    numbers = int(input("Введи число (0 == break) :"))
    three = numbers % 3
    two = numbers % 2
    if numbers != 0:
        if three == 0 and two == 0:
            print("six")
        elif three == 0:
            print("three")
        elif two == 0:
            print("two")
        else:
            print("none")
    else:
        status = False

#1