def guessthenumber():
    import random

    x = random.randint(1, 10)
    guess = int(
        input(
            "Welcome to Guess The Number guess and enter a number to see if that is what the computer was thinking: "
        )
    )
    if x == guess:
        print(x, "was the correct number")
    else:
        print(x, "was the number not", guess, ",hopefully you get it next time")


guessthenumber()
