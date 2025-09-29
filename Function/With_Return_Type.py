#Return Type : Means we have to declare the one function and for calling this function
# we have store into these function in 1 object.
#Then we call this object in print Statement.
from types import CodeType

#Example 1
#function returns single value
print("________________________________#Example 1____________________________________")


def add():
    name="Vikas"
    return name

S1=add()
print(S1)

#Example 2
print("________________________________#Example 2____________________________________")


def add():
    name="Ram"
    Surname="Koli"
    Roll=102
    return name,Surname,Roll

S2=add()
print(S2)

#Example 3
print("______________________________#Example 3______________________________________")

def mul(num1,num2,num4):
    num3=num1*num2*num4
    return num3

S3=mul(10,5,6)
print(S3)


#Example 4
#function returns multiple value
print("________________________________________Example 4____________________________________")

def StudentInfo():
    name="Vikas"
    surname="patil"
    Roll=250
    return name , surname,Roll

nameValue,surnameValue,RollValue=StudentInfo()
print("Student Details::", "Full Name::",nameValue,surnameValue,"Student Roll::",RollValue)
print()
print()
print("Student Details::", "Full Name::",nameValue,surnameValue)
print("Student Roll::",RollValue)


#Example 5
print("________________________________________Example 5____________________________________")

def empInfo():
    Id=121
    City="Pune"
    MobNo=8070903838
    return Id , City , MobNo
    # return City
    # return MobNo  .....We only return all values in single return statement. we cant Take every value in multiple return Statement.


# IdValue =empInfo()
# CityValue=empInfo()
# MobNoValue=empInfo() ...>This is type not allowed in output it will give 3 times result

IdValue ,CityValue,MobNoValue =empInfo()
print("Emp-Id::",IdValue,"___________Emp-City::",CityValue,"_____________Emp-Mobile No::",MobNoValue)
print("________________________________")
print("Emp-Id::",IdValue)
print("Emp-City::",CityValue)
print("Emp-Mobile No::",MobNoValue)


#Example 6
print("________________________________________Example 6____________________________________")

def add ():
    num1=10
    num2=20
    num3=30
    return num1, num2,num3

No1Value , No2Value, No3value=add()
print(No1Value+No2Value+No3value)


print("_________________________________")

def Details(num1,num2):

    add=num1+num2
    mul=num1*num2
    return add,mul

addValue, mulValue=Details(10,20)
print("Addition::",addValue)
print("Multiplication::",mulValue)

print("________________________")
print("Addition::",addValue, "Multiplication::",mulValue)

