# Write a program to find the biggest of 4 numbers.
#    a) Read 4 numbers from user using Input statement.
#    b) extend the above program to find the biggest of 5 numbers.
# (PS: Use IF and IF & Else, If and ELIf, and Nested IF)
mylist = []
for i in range(0,4):
    num = int(input("Enter numbers "))
    mylist.append(num)
print(mylist)
num1 = mylist[0]
num2 = mylist[1]
num3 = mylist[2]
num4 = mylist[3]

print(num1)
print(num2)
print(num3)
print(num4)

if num1 >num2 and num1 > num3 and num1 > num3:
    print("Greatest numbers is ", num1)
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("Greatest number is ", num2)
elif num3> num1 and num3>num2 and num3> num4:
    print("Greatest number is ", num3)
else:
    print("Greatest number is ", num4)

#    b) extend the above program to find the biggest of 5 numbers.

num5 = int(input("Enter 5th Number "))
print(num5)

if num1 >num2 and num1 > num3 and num1 > num4 and num1 > num5 :
    print("Greatest numbers is ", num1)
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("Greatest number is ", num2)
elif num3> num1 and num3>num2 and num3> num4 and num3 > num5:
    print("Greatest number is ", num3)
elif num4 > num1 and num4>num2 and num4> num3 and num4> num5:
    print("Greatest number is ", num4)
else:
    print("Greatest number is ", num5)

