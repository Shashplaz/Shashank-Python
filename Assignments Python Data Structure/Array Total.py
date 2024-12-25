# Assignment 2 : Create 2D Array - Find Total of the Array
from array import *

a1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
for row in a1:
    print(*row, sep="|")

total = 0

for i in a1:
    for j in i:
        total = j + total
print("Total: ", total)
maxes = 0
minmum = 1
for l in a1:
    for p in l:
        if p > maxes:
            maxes = p
for q in a1:
    for x in q:
        if x < minmum:
            minmum = x
            print(minmum)

print("Maximum: ", maxes)
print("Minimum: ", minmum)
