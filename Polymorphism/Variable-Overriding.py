# Ex3: Variable Overriding
#
# Ex3.1: print only override child class variable

class parent:
   name="amol"

class child(parent):
   name="AMOL"

c=child()
print(c.name)

print("___________________________________________________")
# Ex3.2: print both parent & child class variable
class parent1:
   name="amol"

class child1(parent1):
   name="AMOL"

   def test(self):
       name = "AMOL"
       print(super().name)
       print(name)

c=child1()
# print(c.name)
c.test()

