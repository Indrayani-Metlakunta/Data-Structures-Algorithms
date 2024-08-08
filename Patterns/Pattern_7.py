# https://www.geeksforgeeks.org/problems/triangle-pattern-1661492263/1

def printPyramid():
    N = int(input("Enter :"))
    for i in range(N):
        for j in range(N-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print('*', end="")

        print()

printPyramid()

# o/p:
#   *
#  ***
# *****

                


