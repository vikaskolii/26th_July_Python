marks=40

if marks>=55:
    print("Distinction")
elif marks>=50 and marks<55:
    print("A+")
elif marks>=40 and marks<50: #(40,41,42,43,44,45  and <50 )
    print("B+")
elif 35 <= marks < 40:
    print("Pass")
else:
    print("FAIL")
