def sum_of2numbers(Firstnumber, Secondnumber):
    Firstnumberfloat = float(Firstnumber)
    Secondnumberfloat = float(Secondnumber)
    answer = Firstnumberfloat + Secondnumberfloat
    return print("The answer is", answer)


Firstnumber = input("What is the first number you want to add? ")
Secondnumber = input("What is the second number you want to add? ")
sum_of2numbers(Firstnumber, Secondnumber)
