def adds(x, y):
    return x + y


def subtracting(x, y):
    return x - y


def multiplying(x, y):
    return x * y


def dividing(x, y):
    return x / y


def calculator():
    print("Adding: 1")
    print("Subtracting: 2")
    print("Multiplying: 3")
    print("Dividing: 4")
    choice = input(
        "Put the number with the corresponding operation you would like to use: "
    )

    if choice == "1":
        x = float(input("What is the first number would you like to use the add? "))
        y = float(input("What is the second number would you like to use the add? "))
        ans = adds(x, y)
        print(ans)
    elif choice == "2":
        x = float(
            input("What is the first number would you like to use the subtract? ")
        )
        y = float(
            input("What is the second number would you like to use the subtract? ")
        )
        ans = subtracting(x, y)
        print(ans)
    elif choice == "3":
        x = float(
            input("What is the first number would you like to use the multiply? ")
        )
        y = float(
            input("What is the second number would you like to use the multiply? ")
        )
        ans = multiplying(x, y)
        print(ans)
    elif choice == "4":
        x = float(input("What is the first number would you like to use the divide? "))
        y = float(input("What is the second number would you like to use the divide? "))
        ans = dividing(x, y)
        print(ans)
    else:
        print("Error!!! Please type the operator you want to use again")
        calculator()


calculator()
