# i     0   1  2  3  4
arr = [11, 6, 13, 7, 5]
#               j  j+1
no = len(arr)
print("Size is ", no)
print("Before Sorting: ", arr)  #   0  1  2   3   4
# arr = [5, 6, 8,  10, 20 ]
#      j
# i    j     no    no - 1 - i
for i in range(no - 1):  #             5      4
    for j in range(no - 1 - i):  # 1                  3
        #                      # 2                  2
        if arr[j] > arr[j + 1]:  # 3                  1
            t = arr[j]  # 4False
            arr[j + 1] = t
print("After Sorting: ")
print(arr)
