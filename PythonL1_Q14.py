# Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
#      a) Print all names on to screen
#      b) Read the index from the  user and print the corresponding name from both list.
#      c) Print the names from 4th position to 9th position
#      d) Print all names from 3rd position till end of the list
#      e) Repeat list elements by specified number of times (N- times, where N is entered by user)
#      f)  Concatenate two lists and print the output.
#      g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )
from setuptools._vendor.six import print_

mylistEmpidA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylistEmpNameB = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

#      a) Print all names on to screen
for i in range(len(mylistEmpNameB)):
    print(mylistEmpNameB[i])
#      b) Read the index from the  user and print the corresponding name from both list.

userinput = int(input("Please enter any index number between 0 to 9 "))
print("Emp ID is ", mylistEmpidA[userinput])
print("Emp Name is ", mylistEmpNameB[userinput])

#      c) Print the names from 4th position to 9th position
print("names from 4th position to 9th position", mylistEmpNameB[3:9])
#      d) Print all names from 3rd position till end of the list
print("names from 3rd position till end of the list", mylistEmpNameB[2:])
#      e) Repeat list elements by specified number of times (N- times, where N is entered by user)
UserinputIteration = int(input("please enter the number, you want to print the number as many times you want"))
print("List item as many times you want to print", mylistEmpNameB[userinput] * UserinputIteration)

#      f)  Concatenate two lists and print the output.
print("Concatenation of List A and B", mylistEmpidA + mylistEmpNameB)

#      g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

tup1 = mylistEmpidA
tup2 = mylistEmpNameB
res = "\n".join("{} {}".format(x, y) for x, y in zip(tup1, tup2))
print("Printing elements from lists Side by Side------------")
print(res)
