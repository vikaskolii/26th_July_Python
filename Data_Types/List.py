"""
1: List

It like array/ArrayList in java
It can be homogeneous or heterogeneous

1: List contains duplicate Items
2: List Maintain order
3: List is mutable. We can modify/update/insert/remove data
4: List is declared using [ ]
5: data is stored in index format
"""
from operator import index

print("__________________List_____________________")

ls=["Vikas", 120,"Koli",510,65.1,"Pune"]                     # we store Heterogeneous& homogeneous Elements & decleared in [].
print(ls)                                                    # Also list maintain inseration order.


print("__________________List Different Operations_____________________")


print("List data type::",type(ls))                   # Get the data type of the list.

print("List Size::",len(ls))                         # get the size of list

print("Index::",ls[2])                               # Particular Index at the position
print("Index::", ls[4])


print("_________________________________________________________________")
#Add data in list append/insert/extend

ls.append("Ram")                         # add only one element in list . But it will go at last in the list.
ls.append("Vishal")
print(ls)

ls.insert(1,"Vaibhavi")   # add new element at particular index
print(ls)

ls.extend([24,25,"rani"])           #add multiple new elements at the end
print(ls)

#remove data from list -> pop(), pop(index), remove(object/element)
print("_________________________________________________________________")

ls.pop()     #It will remove only last element in the list
print(ls)

ls.pop(1)     # It will remove particular Index element which we mention the index
print(ls)

ls.remove("Ram")  # It will remove only Specific element which we want to remove.
print(ls)

print("_________________________________________________________________")

ls2=ls.copy()
print(ls2)

print("------print all data using for loop------")
for i in ls:
   print(i)

print("---print specific data using for loop---")
for i in range(0,5):   # 0 to 3+1
   print(ls[i])


print("_________________________________________________________________")

