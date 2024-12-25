numbs = [10, 20, 30, 40, 50]
no = int(input("Enter a number: "))

f = False
for i in numbs:
    if i == no:
        f = True
        break

if f == True:
    print("Number in list")
else:
    print("Number not in list")
