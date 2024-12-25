arr = [6, 3, 5, 21, 9]
no = len(arr)
print("Size:", no)
print("Before sorting:", arr)
for i in range(no - 1):
    for j in range(no - 1):
        if arr[j] > arr[j + 1]:
            r = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = r
print("After sorting:", arr)
