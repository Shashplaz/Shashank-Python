def prime(j):
    if j == 1:
        return 0
    s = 2
    o = j - 1

    while s < o:
        l = j % s
        if l == 0:
            return 0
        s = s + 1
    return 1


for p in range(1, 20):
    x = prime(p)
    if x == 1:
        print(p, "is prime")
    else:
        print(p, "is not prime")
