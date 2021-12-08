room1 = int(input("Учнів в 1 класі :"))
room2 = int(input("Учнів в 2 класі :"))
room3 = int(input("Учнів в 3 класі :"))

allChild = room2 + room3 + room1
tables = 0

for i in range(allChild):
    if allChild > 0:
        allChild -= 2
        tables += 1

    elif allChild == 1:
        allChild -= 1
        tables += 1

    else:
        print("Потрібно парт : ", tables)
        break

#1