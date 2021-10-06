def primary(n):
    lst = []
    k = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1

        if k == 0:
            lst.append(i)
        else:
            k = 0
    print(lst)
