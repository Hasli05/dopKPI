def minInArr(arr):
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min


def maxInArr(arr):
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max


arrNumbers = list(input('Введіть числа (без пробілів, ком і т.д): '))

print('Найменше число: ', minInArr(arrNumbers))
print('Найбільше число: ', maxInArr(arrNumbers))

#1