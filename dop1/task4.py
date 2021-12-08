allMinutes = int(input("Введіть скільки хвилин пройшло після 00:00 :"))

if allMinutes <= 1440:
    minutes = allMinutes % 60
    hours = -1

    for i in range(23):
        if allMinutes > 0:
            allMinutes -= 60
            hours += 1

    print("Пройшло ", hours, " годин і ", minutes, " хвилин")

else:
    print("В сутках тільки 1440 хвилини!!!")