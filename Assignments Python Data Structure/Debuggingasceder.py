# i
# 1 3 4 5 6 9
#           j
#                                       numb         i       j      r
#                                        6           0       5 f    9
#                                                    1       5 f    5
#                                                    2       5 f    5
#                                                    5 f
arr = [6, 5, 3, 1, 9, 4]
numb = len(arr)
print("Before:", arr)
for i in range(numb - 1):
    for j in range(numb - 1):
        if arr[j] > arr[j + 1]:
            r = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = r
print("After", arr)
