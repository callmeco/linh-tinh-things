dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

dict2 = dict1.copy()
print(dict2)

dict1.clear()
print(dict1)

print(dict2.get(1))

print(dict2.items())

print(dict2.keys())

dict2.pop(4)
print(dict2)

dict2.popitem()
print(dict2)

dict2.update({3: "Scala"})
print(dict2)

print(dict2.values())
