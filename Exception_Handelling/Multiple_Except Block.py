
a=10
b=0

try:
    print(a/b) #risky code
    # print(a/a)
except ZeroDivisionError:
    print("Zero Division Error occured")
except ValueError :
    print("Value Error")
except IndexError :
    print("Key Error")
    print("This are the errors got ")

