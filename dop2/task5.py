firstDayDist = float(input("Вкажіть дистанцію за перший день :"))
finalDist = float(input("Вкажіть кінцеву дистанцію :"))

status = True

day = 1
tempDist = firstDayDist


while status:
    if tempDist < finalDist:
        distGain = tempDist / 10
        tempDist += distGain
        day += 1
    else:
        status = False
        break

print(day)

#1