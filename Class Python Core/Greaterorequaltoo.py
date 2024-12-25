def greaterthanequal():
    print("Enter two numbers to see if it is greater or equal to")
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if x >= y:
        if x == y:
            print("Both numbers are equal")
        else:
            print(x, "is greater than", y)
    else:
        print(y, "is greater than", x)


greaterthanequal()
