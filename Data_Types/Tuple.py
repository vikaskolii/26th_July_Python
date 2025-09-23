'''
2.Tuple::

1: Tuple contains duplicate Items
2: Tuple Maintain order
*3: Tuple is immutable. We can’t modify/update/insert/remove data
*4: Tuple is declared using ( )
5: data is stored in index format


List & tuple does same thing only diff is
1: Tuple is immutable  (when u declare tuple u cant update it again)
2: Tuple is declared using ( ) & list using [ ]

'''

Tu=(21,22,"Ram",212,"Viki",22)
print(Tu)                      #1.Tuple contains duplicate Items>>>>>>2.Tuple Maintain order>>>>>>>>3.Tuple is declared using ( ).

#Tu[0]=20     # Invalid statement as tuple doesn't allow to update data

print("________________________________________________________________________")
'''
These functions are not available in tuple
append(), insert(), extend(), pop(), remove()
'''
print("Size of the Tuple::",len(Tu))

print("___________________________Particular Element_____________________________________________")

print(Tu[2])  ## Get specific data

print("___________________________Adding element_____________________________________________")

# Tuples are immutable, so you cannot use `.append()`, `.insert()`, or `.extend()`.
# Instead, create a new tuple:
tp = Tu + (4,)
print(tp)  # Output: (6, 5, 0, 'abc', 11.5, 4)

print("__________________________________Removing elements______________________________________")

# —-Removing elements—----
# Tuples are immutable; you cannot use `.pop()` or `.remove()`.
# Instead, create a new tuple excluding the element:
tp = tuple(x for x in tp if x != 11.5)
print(tp)  # Output: (6, 5, 0, 'abc', 4)

print("________________________________Copy tuple________________________________________")

#----Copy tuple—
tp1 = Tu  # Copy by assignment (no `.copy()` method needed for tuples)
print(tp1)  # Output: (6, 5, 0, 'abc', 4)

print("_________________________________Sorting (Tuples cannot be sorted directly)_______________________________________")

# —--Sorting (Tuples cannot be sorted directly)---
tup = (3, 1, 4, 2)
s1= tuple(sorted(tup))  # Creates a new sorted tuple
print(s1)  # Output: (1, 2, 3, 4)

print("____________________________Reversing (Create a new reversed tuple)____________________________________________")

# Reversing (Create a new reversed tuple)
reversed_tup = tup[::-1]
print(reversed_tup)  # Output: (2, 4, 1, 3)

print("_________________________________Searching & Counting_______________________________________")

# Searching & Counting
tp = (1, 4, 8, 6, 4, 6, 2, 8)
print(tp.index(8))  # Output: 2 (1st occurrence)
print(tp.count(4))  # Output: 2
print(tp.count(7))
print(tp.count(1))




