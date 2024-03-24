print("This is a circle area calculator")
r = int(
    input(
        "Please enter the radius of the circle (if you have a the diameter then divide by 2)"
    )
)
a = 3.14 * (r * r)
print(
    "The answer is",
    a,
    "(Note: Pi was rounded to 3.14 so this is just a simplified version of the full answer)",
)
