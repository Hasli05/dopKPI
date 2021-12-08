a = float(input("Відстань між рядами отворів :"))
b = float(input("Відстань між отворами в ряді :"))
l = float(input("Довжина вільного кінця :"))
n = int(input("Кількість отворів в кожному ряді :"))

holes = n * 2

allA = holes - 1
allB = holes - 2

length = (allB * b) + (allA * a) + (l * 2)

print(length)

#1