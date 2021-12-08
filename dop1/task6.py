firstStartStation = int(input("Перша зупинка першого автобусу :"))
firstFinishStation = int(input("Кінцева зупинка першого автобусу :"))

secondStartStation = int(input("Перша зупинка другого автобусу :"))
secondFinishStation = int(input("Кінцева зупинка другого автобусу :"))

intersections = 0
status = True

while status:
    if (firstStartStation <= secondStartStation) and (secondStartStation >= firstFinishStation):
        intersections += 1
        firstStartStation += 1
    elif (firstStartStation >= secondStartStation) and (secondStartStation <= firstFinishStation):
        intersections += 1
        secondStartStation += 1
    else:
        print("Пересічєній : ", intersections)
        status = False
        break

#1



