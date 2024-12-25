class Numbers:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def display(self):
        print(self.n1)
        print(self.n2)


class Arithmetic(Numbers):
    def __init__(self, n1, n2):
        Numbers.__init__(self, n1, n2)

    def addition(self):
        ans = self.n1 + self.n2
        print("Addition:", ans)

    def subtract(self):
        ans = self.n1 - self.n2
        print("Subtraction:", ans)

    def multiplication(self):
        ans = self.n1 * self.n2
        print("Multiplication:", ans)

    def division(self):
        ans = self.n1 / self.n2
        print("Dividing: ", ans)


b1 = Arithmetic(6, 3)
b1.division()
b1.subtract()
b1.addition()
b1.multiplication()
