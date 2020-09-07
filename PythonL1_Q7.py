# Create a list with at least 10 elements having integer values in it;
#        Print all elements
#        Perform slicing operations
#        Perform repetition with * operator
#        Perform concatenation with other list.

#        Print all elements
mylistp1 = [10,65,12,89,47,54,65,98,47,58]
print(len(mylistp1))
for i in range(len(mylistp1)):
    print(mylistp1[i])

#        Perform slicing operations
print(mylistp1[2:6]) # it will print the lists from index 2 till 5

#        Perform repetition with * operator
print(mylistp1[2:6]*5) # it will print the lists from index 2 till 5 , 5 times


#        Perform concatenation with other list.

list2 = [80,90,50]

list3 = mylistp1+list2
print(list3) # it will print concatenated list of mylistp1+list2
