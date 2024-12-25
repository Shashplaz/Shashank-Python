fruits = ["apple", "mango", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break

    print(x)

print("For Continue:")
for x in fruits:
    if x == "cherry":
        continue
    print(x)
