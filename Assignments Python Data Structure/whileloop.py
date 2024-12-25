array = [5, 2, 4, 1, 1, 3, 1]
i = 0
print("Before:", array)
while i < 6:
    j = 0
    while j < 6:
        if array[j] > array[j + 1]:
            r = array[j]
            array[j] = array[j + 1]
            array[j + 1] = r
        j = j + 1
    i = i + 1
print("After", array)
