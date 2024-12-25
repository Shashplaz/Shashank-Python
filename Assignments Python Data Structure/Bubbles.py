# i
# 9 6 5 4 3 1
# j
#                       numb                     i    i<5      j  j<5      r
#                         6                      0             5 f         1
#                                                1             5 f         3
#                                                2             5 f         5
#                                                3             5 f         6
#                                                4             5 f         0
#                                                5 f           0           0
arr = [6, 5, 3, 1, 9, 4]
numb = len(arr)
print("Before:", arr)
for i in range(numb - 1):
    for j in range(numb - 1):
        if arr[j] < arr[j + 1]:
            r = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = r
print("After", arr)
