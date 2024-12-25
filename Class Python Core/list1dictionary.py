def cmp(a, b):
    return (a > b) - (a < b)

# initializing argument lists
list1 = [1, 2, 4, 3]
list2 = [1, 2, 4, 1]

# Comparing lists
print("Comparison of list2 with list1 : ")
x=cmp(list2, list1)
print(x)