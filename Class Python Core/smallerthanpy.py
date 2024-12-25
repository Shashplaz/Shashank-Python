def smaller():
    print("Enter two numbers to see which one is smaller")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if x < y:
        print(x, "is smaller than", y)
    elif y < x:
        print(y, "is smaller than", x)
    else:
        print(x, "and", y, "is equal")


smaller()
