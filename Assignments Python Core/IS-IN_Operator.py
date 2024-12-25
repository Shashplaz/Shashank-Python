"""
is and is not Operators

The is and is not operators are used to check if two variables refer to the same object in memory.

python

# Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Using is operator
print(list1 is list2)  # False, because list1 and list2 refer to different objects
print(list1 is list3)  # True, because list1 and list3 refer to the same object

# Using is not operator
print(list1 is not list2)  # True, because list1 and list2 refer to different objects

2. in Operator

The in operator is used to check if an element exists in a list.

python

# List
fruits = ['apple', 'banana', 'cherry']

# Using in operator
print('apple' in fruits)   # True
print('orange' in fruits)  # False

3. not in Operator

The not in operator is used to check if an element does not exist in a list.

python

# List
fruits = ['apple', 'banana', 'cherry']

# Using not in operator
print('orange' not in fruits)  # True
print('banana' not in fruits)  # False

4. Logical Operators (and, or, not)

Logical operators are used to combine conditional statements.

python

# Lists
numbers = [1, 2, 3, 4, 5]
vowels = ['a', 'e', 'i', 'o', 'u']

# Using and operator
print(len(numbers) > 3 and 'a' in vowels)  # True

# Using or operator
print(len(numbers) > 5 or 'z' in vowels)   # False

# Using not operator
print(not len(numbers) > 5)  # True

Assignment Tasks
Task 1: Check if an element exists in a list and print a message

python

# List
colors = ['red', 'blue', 'green']

# Check if 'blue' exists in colors list
if 'blue' in colors:
    print("Blue color is in the list.")
else:
    print("Blue color is not in the list.")

Task 2: Check if two lists are equal using is operator

python

# Lists
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

# Check if list_a and list_b are equal
if list_a is list_b:
    print("list_a and list_b are the same.")
else:
    print("list_a and list_b are different.")

Task 3: Combine multiple conditions using logical operators

python

# Lists
numbers = [10, 20, 30, 40]
vowels = ['a', 'e', 'i', 'o', 'u']

# Check if the length of numbers is greater than 3 and 'a' is in vowels
if len(numbers) > 3 and 'a' in vowels:
    print("Condition satisfied.")
else:
    print("Condition not satisfied.")
"""

# Task One Work
Animal = ["Monkey", "Cheetah", "Lion"]
if "Cheetah" in Animal:
    print("You don't have a Cheetah")
else:
    print("You don't have a Cheetah")


# Task Two Work
List1 = ["e", "E", "EEEEEEEEEEEEEEEEEEEEEEEEE"]
List2 = ["e", "E", "EEEEEEEEEEEEEEEEEEEEEEEEEEE"]
List3 = List2
if List1 == List2:
    print("List1 is equal to List2")
elif List1 == List3:
    print("List1 is equal to List3")
else:
    print("Nothing is equal")

# Task Three Work

List4 = [10, 9]
List5 = ["Cheeseburger", "Soda"]
if 11 > 10 and "Cheeseburger":
    print("Cheeseburger is in stock")
else:
    print("Cheeseburger is not in stock")
