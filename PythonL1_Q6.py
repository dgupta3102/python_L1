# Write a program to read string and print each character separately.
#     a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
#     b) Repeat the string 100 times using repeat operator *
#     c) Read string 2 and concatenate with other string using + operator.

Word = input("Please Enter the String : ")
sent = Word
for i in range(len(Word)):
    print("The Character at %d Index Position = %c" % (i, Word[i]))


# Slice operation --- starts from 2nd index till n-1 index
print("Slicing-->",sent[2:5])

# b) Repeat the string 100 times using repeat operator *

print("Repeat string 100 times ..",(sent[0:5]*100))



#     c) Read string 2 and concatenate with other string using + operator.
str1 = input("Enter String 1  ")
str2 = input("Enter String 2  ")
# concatenation of 2 strings using + operator
str3 = str1+" "+str2
print(str3)

