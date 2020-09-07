# Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.
mylist = []
for i in range(0,10):
    num = int(input("Enter numbers "))
    mylist.append(num)
    print("List contains {} numbers".format(i+1))
    if i == 10:
        break
print(mylist)
# Read 10 numbers from user and find the average of all.
Avg = sum(mylist)/len(mylist)
print ("Average of all the numbers is ", int(Avg))

# a) Use comparison operator to check how many numbers are less than average and print them
for i in range(len(mylist)):
    if mylist[i] < Avg:
        print("Less than Average number ",mylist[i])

# b) Check how many numbers are more than average.
for i in range(len(mylist)):
    if mylist[i] > Avg:

        print("Greater than Avergae number",mylist[i])
# c) How many are equal to average.
for i in range(len(mylist)):
    if mylist[i] == Avg:

        print("Numbers equal to Average of numbers",mylist[i])