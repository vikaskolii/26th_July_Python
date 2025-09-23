#Before Sorting
print("_________________#Before Sorting______________________")
lst=[20,10,84,5,6]
print(lst)

#After sorting / Ascending order
print("___________________#After sorting____________________")
lst.sort()
print(lst)

#Sort data in descending order
print("___________________#Sort data in descending order____________________")

s1=[80,70,100,55,24]
s1.sort()           # Here we sorting in ascending using function.But there is no direct function for descending.
print(s1)
s1.reverse()        #after sorting we call reverse method for the descending order and then calling in print statment.
print(s1)

print("-------------------------------------------")
print("----------")
#Searching & Counting
s2=[1,5,2,6,7,8,0,2,8,2,1]

print(s2.index(5))   #return index of element ->1st ocurance
print(s2.count(2))   #return ocu/count of element  -> imp
