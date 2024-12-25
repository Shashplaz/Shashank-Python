list = [10, 20, 30, 5, 15, 50]
m = 0
for i in list:
    m = i + m
a = m / len(list)
print("Total:", m)
print("Average:", float(a))
