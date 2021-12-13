def perfectNum():
    for i in range(2, 100000):
        s = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                s += j
        if s == i:
            print(i)


perfectNum()

#10