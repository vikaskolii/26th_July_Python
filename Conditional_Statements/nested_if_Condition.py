# syntax
from selectors import SelectSelector

# if condition1:
# body1
# if condition2:
# body2
# else:
# elseBody2
# else:
# elseBody1



PEM=250

if PEM>=200:
    print("Got selected in Prelim Exam")
    print("And go to Mains exam")

    MEM=450
    if  MEM>=400:
       print("Cracked the Mains Exam")
    else:
       print("Rejected in Mains Exam")

else:
    print("Rejected in Prelim Exam")

# Note= "In Every Python Program Identitaion is Very Very Important"


