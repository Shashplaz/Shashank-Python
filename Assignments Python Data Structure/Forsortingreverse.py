arr = [6, 5, 3, 1, 9, 4]
numb = len(arr)
for i in range(numb - 1):
    for j in range(numb - 1):
        if arr[j] < arr[j + 1]:
            r = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = r
print(arr)
