def vowelchecker(x):
    vowels = ["a", "i", "e", "o", "u"]
    y = []
    for character in x:
        if character in vowels:
            y.append(character)
    count = len(y)
    if count > 0:
        print(x, "has", count, "vowels and they are", y)
    else:
        print("This word is vowel-less ;)")


x = input("This is a vowel checker please enter a word to check if it has a vowel: ")
vowelchecker(x)
