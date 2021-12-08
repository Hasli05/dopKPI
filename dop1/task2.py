ticket = list(input("Введіть номер білету :"))

sum1 = 0
sum2 = 0

for i in range(len(ticket)):
    if i < 3:
        sum1 += int(ticket[i])
    elif (i >= 3) and (i <= 6):
        sum2 += int(ticket[i])

if sum1 == sum2:
    print("Білет щясливий!")
elif sum1 != sum2:
    print("Білет звичайний")
#1
