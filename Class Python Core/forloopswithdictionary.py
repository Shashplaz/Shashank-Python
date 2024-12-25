myDict = {"ravi": 10, "sanjeev": 15, "yash": 2, "suraj": 32}

myKeys = list(myDict.keys())

myKeys.sort()

sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)
print(myKeys)

print(len(myDict))
