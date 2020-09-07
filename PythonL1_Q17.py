# Write program to find the biggest and Smallest of N numbers.
#       PS: Use the functions to find biggest and smallest numbers.
def Smallest():
    print("Print smallest number")
    lst = []
    num = int(input('How many numbers: '))

    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)

    print("Maximum element in the list is :", max(lst))


def Biggest():
    print("Print biggest number")
    lst = []
    num = int(input('How many numbers: '))

    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)

    print("Minimum element in the list is :", min(lst))


Smallest()

Biggest()
