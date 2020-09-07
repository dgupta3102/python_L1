# Create a tuple with at least 10 elements having integer values in it;
#        Print all elements
#        Perform slicing operations
#        Perform repetition with * operator
#        Perform concatenation with other list.

#        Print all elements
mytuple = (10,65,12,89,47,54,65,98,47,58)
print(len(mytuple))
for i in range(len(mytuple)):
    print(mytuple[i])

#        Perform slicing operations
print(mytuple[2:6]) # it will print the tuple from index 2 till 5

#        Perform repetition with * operator
print(mytuple[2:6]*5) # it will print the lists from index 2 till 5 , 5 times


#        Perform concatenation with other list.

mytuple2 = (80,90,50)

mytuple3 = mytuple+mytuple2
print(mytuple3) # it will print concatenated list of mylistp1+list2
