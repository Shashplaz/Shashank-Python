name = input("Enter a word: ")
revname = ""
for i in name:
    revname = i + "" + revname

if revname == name:
    print(
        name,
        "is a palindrome because it spelt backwards is",
        revname,
        "which is the same thing",
    )
else:
    print(
        name,
        'Not a palindrome because it spelt backwards is"',
        revname,
        '"which is the same thing',
    )
