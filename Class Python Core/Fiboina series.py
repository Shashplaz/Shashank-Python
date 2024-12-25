n = 10
p = 0
a = 1
next = a
count = 1
while count <= n:
    print(next, end=" ")
    count += 1
    p, a = a, next
    next = p + a
print(next)
