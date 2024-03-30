def palidinrome():
    x = "pup"
    y = []
    for palidinromewd in x[::-1]:
        y.append(palidinromewd)
    print(y)
    w="".join(y)
    print(w)
    if x == w:
        print(x, "is palidinrome")
    else:
        print(x, "is not palindirome")


palidinrome()
