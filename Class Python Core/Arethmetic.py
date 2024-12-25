def adding():
    print("Enter two numbers to add")
    x = input("First Number: ")
    y = input("Second Number: ")
    xwas = int(x)
    ywas = int(y)
    a = xwas + ywas
    print("Your answer is", a, ".")


def subtracting():
    print("Enter two numbers to subtract")
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    xw = int(x)
    yw = int(y)
    a = xw - yw
    print("Your answer is", a, ".")


def multiplying():
    print("Enter two numbers to multiply")
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    xww = int(x)
    yww = int(y)
    a = xww * yww
    print("Your answer is", a, ".")


def dividing():
    print("Enter two numbers to divide")
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    xwww = int(x)
    ywww = int(y)
    a = xwww / ywww
    print("Your anwser is", a)


def remainder():
    print("Enter two numbers to find the remainder")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    a = x % y
    print("Your remainder is", a)


remainder()
