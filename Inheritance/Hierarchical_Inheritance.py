"""Ex3:Hierarchical Inheritance: 
multiple sub classes can acquire properties of 1 super class is known as hierarchical Inheritance. 
"""""

class Father:
   def car(self):
       print("method car from father class")

   def money(self):
       print("method money from father class")

   def home(self):
       print("method home from father class")

class Son1(Father):
   def bike(self):
       print("Bike: FZ V3 from Son1 class")


class Son2(Father):
   def laptop(self):
       print("HP Laptop from Son2 class")

print("------Features of Son1-----")
s1=Son1()
s1.car()
s1.money()
s1.home()
s1.bike()

print("------Features of Son2-----")
s2=Son2()
s2.car()
s2.money()
s2.home()
s2.laptop()

