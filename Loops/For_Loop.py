
print("----print num from 1 to 5------")
# for increment   startNum,EndNum+1, incrValue
#start num=1
#end num=5
#incr/decr=1

#   i=5          6<6
for i in range(1,6):                #by default 3rd parameter=1
    print(i)

print("----print num from 1 to 20------")
for i in range(1,21,1):
    print(i)

print("----print num from 5 to 30------")
for i in range(5,31):
    print(i)


print("----print table of any num------")
for i in range(1,11):
    print(i*9)


print("----print num from 2 to 20, incr by 2------")
#     i=4       8<21
for i in range(2,21,2):
    print(i)

print("----print num from 5 to 50, incr by 5------")
for i in range(5,51,5):
    print(i)


print("----print num from 5 to 1------")
# for decrement   startNum,EndNum-1, decrValue
#             0>0
for i in range(5,0,-1):
    print(i)


print("----print num from 20 to 8------")
for i in range(20,7,-1):
    print(i)


print("----print num from 20 to 8 with decr of 2------")
for i in range(20,7,-2):
    print(i)

print("----print msg multiple time------")
#             6<6
for i in range(1,21):
    print("Hi")

# Hi
# Hi
# Hi
# Hi
# Hi

print("----print square of num from 1 to 5------")

for i in range(1,21):
    print(i*i)

