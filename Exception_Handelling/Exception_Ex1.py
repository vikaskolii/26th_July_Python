#Normal exception
"""
ZeroDivisionError → dividing by zero
ValueError → invalid type/format (e.g., int("abc"))
IndexError → accessing invalid list index
KeyError → accessing missing dictionary key
FileNotFoundError → trying to open a file that doesn’t exist
TypeError → invalid operation between incompatible types

"""

#1.ZeroDivisionError
# it is occured when the division amt become zero .
from csv import excel

a=10
b=0

print("Program started")

try:
    print(a/b)    #risky code
except ZeroDivisionError as e:
    print("ZeroDivisionError is occured")

    print("___________________________________")
    print("___________________________________")



#Normal exception ex 2

a=10
b=0

print("Program started")

try:
    print(a/b)  #risky code
except ZeroDivisionError as e:
    print(a/1)
    print("___________________________________")
    print("Hi Vikas")
    print("ZeroDivisonError Is occured")


#2.Value error
try:
    num = int("abc")  # invalid conversion
except ValueError:
    print("___________________________________")
    print("___________________________________")
    print("❌ Invalid format, cannot convert to integer")


    try:
        num=int("Ram")
    except ValueError:
        print("__________________________________")
        print("__________________________________")
        print(" inavalid Format & These type of error is value type error")

# 3.File not Found error
print("__________________________________")
print("__________________________________")
try:
    f = open("non_existing_file.txt", "r")  # file doesn’t exist
except FileNotFoundError as e:
    print("❌ File not found")
    print("File not found error")

print("__________________________________")
print("__________________________________")

try:
    f=open("non existing file.txt", "r")
except FileNotFoundError:
    print("❌ File not found")
    print("File not found error")


#4.Type Error

print("__________________________________")
print("__________________________________")
try:
    result = "hello" + 5  # cannot add string and int
except TypeError as e:
    print("❌ This is a Typerror & Unsupported operation between str and int")

print("__________________________________")
print("__________________________________")
try:
        a="Ram"+ 10  # cannot add string and int
except TypeError as e:
    print("This is a Type-Error ." , e)

#5.Index Error

print("__________________________________")
print("__________________________________")

try:
    my_list=[1,2,5,4]
    print(my_list[5])
except IndexError :
    print("This is a Index error")

print("__________________________________")
print("__________________________________")

try:
        my_list=["Ram ", 121 , 45, "#ytr"]
        print(my_list[8])
except IndexError as e:
        print("This is Index error where the index is out of the list" , e)
        print("________+++++++++++============")


#Key error

try:
    my_dict = {"name": "Vikas"}
    print(my_dict["rutuja"])  # key doesn’t exist
except KeyError :
    print("Key Error occured:")

print("________+++++++++++============")
print("________+++++++++++============")


try:
    my_dict = {"name":"Vikas" , "rutuja":121 }
    print(my_dict["age"])  # key doesn’t exist
except KeyError as e:
    print("❌ Error:", e)










