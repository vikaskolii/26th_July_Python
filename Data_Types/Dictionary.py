"""6: Dictionary 
Data is stored in key & value format
Keys must be unique and immutable (e.g., str, int, tuple).
Values can be of any data type and duplicates are allowed.

Dictionaries are unordered in Python 3.6 and earlier; they maintain insertion order from Python 3.7+.
"""""

print("__________________This is the Whole Dictionary____________")
Dictionary={121:"ram",122:"Vishal",123:456,124:"Koli"}
print(Dictionary)

print("__________This the length of the Dictionary______________")
print(len(Dictionary))

print("_____________This is the type of these dictionary______________")
print(type(Dictionary))

print("------get value of specific key------")
print(Dictionary[122])

print("___________Add new K_V pair_______________")
Dictionary[5]="Vikas koli"
print(Dictionary)

print("__________________Update/modify value___________")
Dictionary[123]=852
print(Dictionary)

print("___________Remove any K-V pair______________")
Dictionary.pop(124)
print(Dictionary)

print("___________Remove last k-v pair____________________")
Dictionary.popitem()
print(Dictionary)

print("__________Check if key exist or not___________")
print(123 in Dictionary)
print(127 in Dictionary)
print(785 in Dictionary)

print("__________________get all keys________________")
print(Dictionary.keys())
for key in Dictionary.keys():
   print(key)

print("___________For loop______________")
for i in Dictionary:
    print(i)

print("____________get all values____________")
print(Dictionary.values())
for values in Dictionary.values():
    print(values)

print("_____________all keys & values___________")
print(Dictionary.keys(), Dictionary.values())
for key, values in Dictionary.items():
    print(key, values)

