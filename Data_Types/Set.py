'''''''''
3: Set

List Allow duplicate & set doesn’t allow duplicate values
List maintain order & set doesn’t maintain order
List support indexing & set does not support indexing
Set is declared using { }
'''

print("_____________________________________________________________________________________________")
# Creating a set
st = {6, 5, 0, "abc", 11.5}

print("_____________________________________________________________________________________________")

# Get size of set
print(len(st))  # Output: 5

print("_____________________________________________________________________________________________")

# Accessing elements — ❌ Not possible via index
# Example: print(st[1])  --> Error
# Instead, convert to a list if you need indexed access
print(list(st)[1])  # Example workaround

print("_____________________________________________________________________________________________")

# ------Adding Elements----------
st.add(4)
print(st)  			# Output: {0, 4, 5, 6, 'abc', 11.5} (Order may vary)

print("_____________________________________________________________________________________________")

# Add multiple elements
st.update([-5, -6])
print(st)  			# Output: {0, 4, 5, 6, 'abc', 11.5, -5, -6}

print("_____________________________________________________________________________________________")

# ------Removing Elements----------
st.remove(11.5) 			 # Removes specific element
print(st) 				 # Output: {0, 4, 5, 6, 'abc', -5, -6}

print("_____________________________________________________________________________________________")

st.discard("xyz")  			# No error even if the element doesn't exist
print(st) 				 # Same output (no change)

print("_____________________________________________________________________________________________")

# Using `.pop()` — Random element gets removed
removed_item = st.pop()
print(f"Removed item: {removed_item}")
print(st)

print("_____________________________________________________________________________________________")

# ------Copying Set----------
st1 = st.copy()
print(st1)  			# Output: Copy of the set

print("_____________________________________________________________________________________________")

# ------Sorting Set----------
# Since sets are unordered, use `sorted()` to get a sorted list
# sorted_set = sorted(st)
# print(sorted_set)  # Output: Sorted list (e.g., [-6, -5, 0, 4, 5, 6, 'abc'])

print("_____________________________________________________________________________________________")

# ------Searching & Counting----------
# `.index()` and `.count()` are **not available** for sets
# Instead, use:
print(4 in st)  # Output: True (Check for presence)

print("_____________________________________________________________________________________________")

# ------Clearing Set----------
st.clear()
print(st)  # Output: set()

print("_____________________________________________________________________________________________")

# ------Deleting Set----------
del st
# print(st)  # ❌ Error: NameError (because st no longer exists)

print("_____________________________________________________________________________________________")

print("------Convert Set to list----")
s4={50,30,20,40,10}
print(type(s4))

print("_____________________________________________________________________________________________")

s5=list(s4)                  #  convert set to list
print(type(s5))
print(s5)
print(s5[0])

print("_____________________________________________________________________________________________")

print("------reverse operation----")
s5.reverse()
print(s5)
