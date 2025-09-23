# Method Overriding:
# sub/derived class provides a specific implementation of a method that is already defined in its base class or parent class.
#
# Before performing Method Overriding 1st we need to perform inheritance
#
# Example1
class GrandFather:
   def home(self):
       print("1 BHK")

   def money(self):
       print("1 Lakh")

class Father(GrandFather):
   def home(self):
       print("2 BHK")

   def money(self):
       print("2 Lakh")

class Son(Father):
   def home(self):
       print("3 BHK")

   def money(self):
       print("3 Lakh")


f=Father()
f.home()
f.money()

s=Son()
s.home()
s.money()

g=GrandFather()
g.home()
g.money()

