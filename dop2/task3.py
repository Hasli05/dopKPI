def sumDigitInArr(arr):
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])
    return sum


firstNum = list(input("Введіть 1 число :"))
secondNum = list(input("Введіть 2 число :"))
thirdNum = list(input("Введіть 3 число :"))

firstSum = sumDigitInArr(firstNum)
secondSum = sumDigitInArr(secondNum)
thirdSum = sumDigitInArr(thirdNum)

print("Найбільша сумма : ", max(firstSum, secondSum, thirdSum))

#1