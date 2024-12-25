# Assignment 2: Person ( Parent Class ) -> Employee ( Child Class )
# Person has fname, lname and display()
# Employee inherits Person also it has unique property  (salary) , display()
# Create Object e1 and e2 of Employee class and Display all information


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def show(self):
        print(self.fname)
        print(self.lname)


class Employee(Person):
    pass

    def __init__(self, fname, lname, salary):
        Person.__init__(self, fname, lname)
        self.salary = salary

    def show(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)
        print("Salary: ", self.salary)


print("---> Employee 1 <----")
e1 = Employee("Shashank", "Sathiskumar", "$78")
e1.show()

print("----> Employee 2 <----")
e2 = Employee("Ginger", "Le", "$34")
e2.show()
