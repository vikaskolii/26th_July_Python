#positional parameter
#Def: In that the inseration order is preserved .If we try to call Unsorted way the output will be print that way n Msg.
print("_____________ positional parameter____________________")
def StudentInfo(FN,LN ,ROLL):
    print("Student Name ::", FN)
    print("Student Surname::", LN)
    print("Roll Number::", ROLL)

StudentInfo("Vikas","Koli" ,120) # Inseration order is Preserved
print("_________________________________")
StudentInfo(120,"Vikas", "Koli") # The inseration order is not Preserved .


#Default/Optional Parameter
#Def : when we give default value in function the value is automatically print without calling in print statement.
# It work like "Final" keyword in Java.
print("_________________________________Default/Optional Parameter________________________________________")
def EmpInfo(Id,Fn="Ram",Mob=8070909093):
    print("EmpId::", Id)
    print("Emp Name::", Fn)
    print("Emp Contact::" , Mob)

EmpInfo(1452)
print("_________________________________")
EmpInfo(121)


#Keyword Parameter
#Def: When we dont have the sorting way or we dont have inseration order is not preserved then we go with this parameter.
#In that the inseration order is not preserved .So we directly call at any point in Print Statement.
#In that statement we call at any eay the inseration is not being counted..cause we declere the way of sorting in "print" statement i.e
#we use Keyword parameter.

print("______________________#Keyword Parameter___________________________")

def CustInfo(FN,LN,CITY):
    print("Name::",FN)
    print("Surname::", LN)
    print("City::",CITY)

CustInfo(CITY="Pune", LN="Patil", FN="Rutuja")