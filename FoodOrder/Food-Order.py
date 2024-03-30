# function to greet user
def Greeting(x):
    print("Welcome to A+", x, "!")
    return x


# function to order food
def menu_option(menu_choice):
    # input("What would you like to order. pizza, burger, briyani: ")
    menu = {"pizza": 12, "burger": 3, "briyani": 20}
    if menu_choice in menu:
        return menu[menu_choice]
    else:
        print(
            "Are you stupid, this is A+ not Failure I am going to reset this online order sign in again bozo"
        )
        return exit()


# caluclate tax
def tax(bill):
    total_bill = (bill * 0.15) + bill
    return float(total_bill)


# confirming the order
def confimation(confirming):
    if confirming == ("yes"):
        return print(
            "Your order has been confirmed thank you for ordering from A+ on your next exam you will be getting A+"
        )
        print("Thank you for ordering from A+")
    else:
        return print(
            "Sorry, your order wasn't confirmed because you said no or because you said something else YOU BOZO"
        )


x = input("Hello I am A+'s order ai! Welcome to A+ could you please state your name? ")
Greeting(x)
y = input("What would you like to order. pizza, burger, briyani: ")
z = str(y)

print("sure your choice is", y, "and the cost of this item is", "$", menu_option(z))
print("Lets calculate your bill with tax")
print("beep beep beep")
bill = menu_option(z)
print("This is your", tax(bill))
confirming = input('Please confirm your order by saying "yes"')
confimation(confirming)
