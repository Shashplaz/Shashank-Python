def addition():
    x = int(input("Enter the first number to add "))
    y = int(input("Enter the second number to add "))
    a = x + y
    print("Your answer is", a)


def subtraction():
    x = int(input("Enter the first number to subtract "))
    y = int(input("Enter the second number to subtract "))
    a = x - y
    print("Your answer is", a)


def multiplication():
    x = int(input("Enter the first number to multiply "))
    y = int(input("Enter the second number to multiply "))
    a = x * y
    print("Your answer is", a)


def division():
    x = int(input("Enter the first number to dividing "))
    y = int(input("Enter the second number to dividing "))
    a = x / y
    print("Your answer is", a)


subtraction()
addition()
multiplication()
division()


def rectanglearea():
    print("This is an area of rectangle solver")
    l = int(input("Please input the length:"))
    w = int(input("Please input the width:"))
    b = l * w
    print(
        "The length is",
        l,
        "and the width is",
        w,
        "and the area of this rectangle is",
        b,
    )


rectanglearea()
