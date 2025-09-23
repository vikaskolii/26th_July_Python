day=7

match day:
    case 1:
        print("Today is mon")
    case 2:
        print("Today is Tue")
    case 3:
        print("Today is Wed")
    case 4:
        print("Today is Thr")
    case 5:
        print("Today is Fri")
    case 6 | 7:
        print("Today is Sat")
    case 8 | 9 | 10:
        print("Today is Sun")
    case _:
        print("Invalid input")

#we can use multiple case statements also

