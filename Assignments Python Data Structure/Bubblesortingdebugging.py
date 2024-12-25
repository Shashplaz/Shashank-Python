#           i
# 6 5 3 1 9 4
#           j
#                  numb
#                   6
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
