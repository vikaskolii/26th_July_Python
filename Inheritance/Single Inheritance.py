# 1: Single Level Inheritance: -
# It is an operation where inheritance takes place between only 2 classes.
# To perform single level inheritance only 2 classes are mandatory.

class Father:
   def car(self):
       print("method car from father class")

   def money(self):
       print("method money from father class")

   def home(self):
       print("method home from father class")


class Son(Father):
   def bike(self):
       print("Bike: FZ V3 from Son class")

s=Son()
s.car()
s.money()
s.home()
s.bike()
