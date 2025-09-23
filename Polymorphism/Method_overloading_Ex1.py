"""""""""
Method Overloading:
Declaring multiple method with same method name but with different argument/parameter/inputs 
in a same class is called  method overloading


PolyMorphism concept we can implement using overloading concept
Not completely supported in python just like java, somehow we can achieve polymorphism

"""""""""

#Example of method overloading (Same method with different parameter in same  class)

# EX1:
class Demo:

   def add(self,a=0, b=0,c=0,d=0):
       print(a+b+c+d)

d=Demo()
d.add()
d.add(10,20)
d.add(10,20,30)
d.add(10,20,30,40)

print("_________________________________Example 2__________________________________________")
# EX2:
class Sample:

   def printName(self,sName="xyz"):
       print(sName)

s=Sample()
s.printName()
s.printName("Mahesh")
s.printName("Vikas")
s.printName(121)

