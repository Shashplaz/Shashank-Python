def lessthanequalto():
    print("Enter two number to see if it is less than or equal")
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if x <= y:
        if x == y:
            print(x, "equal to", y)
        else:
            print(x, "is smaller than", y)
    else:
        print(y, "is smaller than ", x)


lessthanequalto()
