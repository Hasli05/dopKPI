for i in range(1000, 10000):
    c = 0
    k = i
    while k > 0:
        u= k % 10
        k= k // 10
        c= c + u
    if c == 15:
        print(i)

#1