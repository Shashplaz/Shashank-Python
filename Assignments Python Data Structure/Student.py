# Comparing the Marks of the 2 Students and print the Student name which has scored maximum marks.


class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def show(self):
        print(self.name)
        print(self.mark)

    def compare(self, stud):
        if self.mark > stud.mark:
            print(self.name, "has the most marks with", self.mark)
        elif stud.mark > self.mark:
            print(stud.mark, "has the most marks with", stud.mark)
        else:
            print("Equal marks")


s1 = Student("Shashank", 97)
s2 = Student("Nikkallas", 73)
s1.compare(s2)
