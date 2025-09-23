#.finally – (Optional) Executes code regardless of whether an exception occurs.

a=10
b=5
c=0

try:
   c=a/b #0=10/5
except:
    print("Exception handelled")
finally:
    print("Running Finally Block")
    #print(c=a/b)
    print(c)
    print("Hello world")