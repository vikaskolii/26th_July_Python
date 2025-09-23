# Generic exception


a=10
b=0

try:
    print(a/b)
except Exception as e:
    print("This is the Error", e)

    # when we use "e" . then the particular exception name display in output.( if we dont know which exceptio we got ).

print("_______________________________")
print("_______________________________")

try:
    my_list=[2, 3 ,5]
    print(my_list[6])
except Exception as e:
    print("This is the Error we Got.", e)

print("_______________________________")
print("_______________________________")


print("--------5: Alternative way of using Generic exception-------------")
a=10
b=0
try:
   print(a/b)
except :
   print("Exception Handled")
print("Hi Hello")
