# Create List - Insert, Remove, Print List using For and Print List using Index in python
l = ["Strawberry", "Banana", "Cherry", "Apple"]
#       0            1            2        3
# Insert multiple items to the list
l.insert(2, "Mangoes")
l.insert(4, "Onion")
l.insert(3, "Orange")
print(l)
# Remove List with for loop and .remove
for r in range(0, len(l) - 1):
    if l[r] == "Cherry":
        l.remove("Cherry")
print(l)
# Print list with index and len
print(l[3])

print(l[len(l) - 1])
