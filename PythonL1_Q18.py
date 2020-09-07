# Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
# a) By using For loop
# b) By using while loop
# c) Let mystring ="Hello world"
# print each character of mystring in to separate line using appropriate loop structure
def forloopprint():
    print("Print numbers from 1 to 100 ")
for i in range(1,101):
    print (i)
# print in reverse order
print("**print from 100 to 1 in reverse order*************************************")
for j in range(100,0,-1):
           print(j)

def whileloopprint():
    print("Using while loop")
    n = 100
    i = 0
    while i < n:
        i = i + 1
        print(i)
    print("Using while loop in reverse order")
    n = 1
    i = 101
    while i > n:
        i = i - 1
        print(i)

def printHello():
    mystring = "Hello World"
    for item in mystring:
        print(item)

forloopprint()
whileloopprint()
printHello()