# Ex2: Method Overriding With Super()
class A:
   def m1(self):
       print("method m1 from parent class")


class B(A):
   def m1(self):
       super().m1()
       print("method m1 from child class")

d=B()
d.m1()
