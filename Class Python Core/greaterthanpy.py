def greater():
    print("Enter two numbers and see which one is bigger")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if x > y:
        print(x, "is greater than", y)
    elif y > x:
        print(y, "greater than", x)
    else:
        print(x, "and", y, "is equal")


greater()
