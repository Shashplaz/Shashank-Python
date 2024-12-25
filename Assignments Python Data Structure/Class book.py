class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name)
        print(self.marks)


s1 = Student("Shashank", 97)
s2 = Student("Rico", 14)
s1.show()
