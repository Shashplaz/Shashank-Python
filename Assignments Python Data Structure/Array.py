# Import * from array libray
from array import *

# Create a 3x4 array
array1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Printing array in 2d format
for row in array1:
    print(*row, sep=" ")
# Inserting new array in to second row
array1.insert(2, [13, 14, 15, 16])
# Printing to check insert is successfully
for row in array1:
    print(*row, sep=" ")
array1.insert(3, [17, 18, 19])
for row in array1:
    print(*row, sep="|")
# We are deleting one row using index
del array1[3]
for row in array1:
    print(*row, sep=",")
a2 = [[10, 10, 10, 10], [5, 5, 5, 5], [9, 9, 9, 9]]
for los in a2:
    print(*los, sep=",,")
# We make and delete a second array
del a2
print(a2)
