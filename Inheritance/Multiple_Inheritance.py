"""
4. Multiple Inheritance:
1 subclass acquiring properties of 2 super classes at the same time is known as Multiple Inheritance.
"""""

class A:
   def m1(self):
       print("Method m1 from A class")


class B:
   def m2(self):
       print("Method m2 from B class")


class C(A,B):
   def m3(self):
       print("Method m3 from C class")

print("------Features of class C-----")
c=C()
c.m1()
c.m2()
c.m3()
