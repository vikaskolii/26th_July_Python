PEM=400

#   400>=300
if PEM>=300:            #outer if
    print("selected in prelim Exam")
    print("preparing for mains Exam")

    MEM=900
    #  900>=800
    if MEM>=1000:                #nested or inner if
        print("got selected in mains Exam")
    else:
        print("Rejected in main Exam")

else:
    print("Rejected in prelim exam")
# Note= "In Every Python Program Identitaion is Very Very Important"
