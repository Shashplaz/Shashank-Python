class Arithmetic:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def show(self):
        print(self.n1)
        print(self.n2)


class MyAddition(Arithmetic):
    def __init__(self, n1, n2):
        Arithmetic.__init__(self, n1, n2)

    def add(self):
        ans = self.n1 + self.n2
        print("Addition:", ans)


b1 = MyAddition(1, 2)
b1.show()
b1.add()


class MySubtraction(Arithmetic):
    def __init__(self, n1, n2):
        Arithmetic.__init__(self, n1, n2)

    def subtract(self):
        ans = self.n1 - self.n2
        print("Subtraction:", ans)


b2 = MySubtraction(1, 2)
b2.show()
b2.subtract()


class MyMultiplication(Arithmetic):
    def __init__(self, n1, n2):
        Arithmetic.__init__(self, n1, n2)

    def multiplying(self):
        ans = self.n1 * self.n2
        print("Multiplication:", ans)


b3 = MyMultiplication(7, 8)
b3.show()
b3.multiplying()


class MyDivision(Arithmetic):
    def __init__(self, n1, n2):
        Arithmetic.__init__(self, n1, n2)

    def division(self):
        ans = self.n1 / self.n2
        print("Division:", int(ans))


b4 = MyDivision(6, 2)
b4.show()
b4.division()
