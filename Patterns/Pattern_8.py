# https://www.geeksforgeeks.org/problems/triangle-pattern-1661493231/1

def printTriangle():
    N = int(input("enter:"))
    for i in range(N):
        for j in range(i):
            print(" ",end="")
        for j in range(2*N-2*i-1):
            print("*",end="")
        print()

printTriangle()

# op:
# *****
#  ***
#   *
