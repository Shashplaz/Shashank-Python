def adding(x, y):
    ans = x + y
    print(ans)


def substracting(x, y):
    ans = x - y
    print(ans)


def multiply(x, y):
    ans = x * y
    print(ans)


def dividing(x, y):
    ans = x / y
    print(ans)


def calculator():

    print("Adding: 1")
    print("Subtract: 2")
    print("Multiplying: 3")
    print("Dividing: 4")
    choice = input("Enter Choice: ")
    x = float(input("What is the number do you want to input: "))
    y = float(input("What is the other number do you want to input: "))
    if choice == "1":
        adding(x, y)
    elif choice == "2":
        substracting(x, y)
    elif choice == "3":
        multiply(x, y)
    elif choice == "4":
        dividing(x, y)


calculator()
