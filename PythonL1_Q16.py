# Write program to perform following:
#      i) Check whether given number is prime or not.
#     ii) Generate all the prime numbers between 1 to N where N is given number.

numberinput = int(input("Enter number to check prime or not "))

if numberinput >1:
    print("Number is ",numberinput)
    for i in range(2,numberinput):
        if numberinput%i:
            print("number is not a prime")
            break
        else:
            print("Number is Prime")
else:
    print("Number is not a prime number",numberinput)


#     ii) Generate all the prime numbers between 1 to N where N is given number.
InputN = int(input("Enter the range to print prime numbers "))
for num in range(1,InputN):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)