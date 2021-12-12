a = int(input("Введіть число a :"))
b = int(input("Введіть число b :"))
c = int(input("Введіть число c :"))

if (a < 0) and (b >= 0) and (c >= 0):
    print("Yes")
elif (a >= 0) and (b < 0) and (c >= 0):
    print("Yes")
elif (a >= 0) and (b >= 0) and (c < 0):
    print("Yes")
else:
    print("No")

#1