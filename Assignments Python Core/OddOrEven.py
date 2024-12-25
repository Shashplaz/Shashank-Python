def oddoreven(number):
    answer = number % 2
    if answer == 0:
        print("Your number is even!")
    else:
        print("Your number is odd!")


number = int(input("What number would you like me to check either it is odd or even? "))
print(number)
oddoreven(number)
