import random

trueNumber = random.randint(1, 100)
status = 0
victory = 0
for status in range(10):
    userNumber = int(input('Вибери число від 1 до 100: '))

    if userNumber == trueNumber:
        print("Ви перемогли!!")
        victory = 1
        break
    elif userNumber > trueNumber:
        print("Загадане число меньще за ваше")
        continue
    elif userNumber < trueNumber:
        print("Загадане число більше за ваше")

if victory == 0:
    print('Ви програли!')
print('Завершення....')

#1