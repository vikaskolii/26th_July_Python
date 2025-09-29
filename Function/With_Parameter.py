#Example 1

def add(num1,num2):
    print(num1+num2)

add(20,30)
print("__________________________________________________")

#Example 2

def mul(num1 , num2, num3):
    print(num1*num2*num3)
print("The Multiplication Is" )
mul(10,5,2 )
mul(110,55,20 )
mul(1,5,12)

print("__________________________________________________")

#Example 3
# Function with parameter String Type

def StudentInfo(FN,LN):
    print("Name:",FN)
    print("Surname:",LN)
StudentInfo("Vikas", "Koli")


#Example 3
# Function with all type of parameter
print("____________________________")

def StudentInfo(Fn, Ln, Grd, Marks,MobNo):
    print("Students Information :::", "Full Name ::",Fn,Ln,"Grd::",Grd,"Marks::",Marks,"Mobile Number::",MobNo)

StudentInfo("Vikas","Koli","A+", 500,8070909093)
StudentInfo("Amit","Mali","C+", 400,8070903838)
