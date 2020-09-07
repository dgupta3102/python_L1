# Using loop structures print even numbers between 1 to 100.
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
#     i) Break the loop if the value is 50
print("part 1a --------------")
for j in range(1, 101):

    if j % 2 != 0:  # checks the number is Odd and Pass
        pass
    else:
        print(j)  # prints the number
        if j == 50:  # checks if the number is 50
            break  # it will break the loop and come out

#     ii) Use continue for the values 10,20,30,40,50
print("Part 2")
for i in range(1, 101):
    # print(i)
    if i % 2 == 0:  # checks the number is even
        print(i)  # prints the number
        if i == 10:
            continue
        elif i == 20:
            continue
        elif i == 30:
            continue
        elif i == 40:
            continue
        elif i == 50:  # checks if the number is 50
            break  # it will break the loop and come out
