# Create a list of 5 names and check given name exist in the List.
#         a) Use membership operator (IN) to check the presence of an element.
#         b) Perform above task without using membership operator.
#         c) Print the elements of the list in reverse direction.

mynamelist = ["Dharmendra","Kartik","Jyoti","Nisha","Kelly"]

checklist = "Kelly"
for item in mynamelist:
    if checklist in mynamelist:
        print("Element present in the list",checklist)
        break
    else:
        print("Element not present in the list")


#         b) Perform above task without using membership operator.
for i in mynamelist:
    if (i==checklist):
        print("Element present in list", checklist)
        break
    else:
        print("Element not present in list",checklist)
#         c) Print the elements of the list in reverse direction.
print("Reversed order of a list",mynamelist[::-1])