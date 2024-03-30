# Middle Name not there or there
def Name():
    first_name = input("What is your first name? ")
    middle_name = input(
        "What is your middle name? if you don't have one then type none "
    )
    last_name = input("What is your last name ")
    if middle_name == "none":
        return print("Hello!, ", first_name, last_name)
    else:
        return print("Hello!, ", first_name, middle_name, last_name)


Name()
