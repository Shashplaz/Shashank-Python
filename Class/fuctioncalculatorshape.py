def triangle(b, h):
    print("This is a triangle calculator")
    # b = int(input("Please enter the base of the triangle: "))
    # h = int(input("Please enter the height of the triangle: "))
    a = b * h * (1 / 2)
    print("The triangle's area is", a, "square units")


def rectangle(l, w):
    print("This is an area of rectangle solver")
    b = l * w
    print(
        "The length is",
        l,
        "and the width is",
        w,
        "and the area of this rectangle is",
        b,
    )


def circle(r):
    print("This is a circle area calculator")
    a = 3.14 * (r * r)
    print(
        "The answer is",
        a,
        "(Note: Pi was rounded to 3.14 so this is just a simplified version of the full answer)",
    )


def square(s):
    print("This is a square area calculator")
    s = int(input("Please enter one of the sides of the square: "))
    a = s * s
    print("The area of the square is", a)


triangle(2, 3)
rectangle(2, 2)
circle(2)
square(2)
