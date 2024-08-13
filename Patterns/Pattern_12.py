# https://www.naukri.com/code360/problems/number-crown_6581894?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&count=25&page=1&search=&sort_entity=order&sort_order=ASC


def numberCrown():
    n = int(input("Enter:"))
    for i in range(1,n+1):
        for j in range(i):
            print(j+1, end=" ")
        for j in range(2*n-2*i):
            print(" ", end = " ")
        for j in range(i, 0, -1):  # i is initialisation, 0 is condition, checks if i>0 and -1 is the decrement.
            print(j, end = " ")

        print()

numberCrown()