# https://www.geeksforgeeks.org/problems/triangle-number-1661428795/1

def printTriangle():
    N = int(input("Enter :"))
    for i in range(1,N+1):
        for j in range(N-i+1):
            print('*', end=" ")
        print()

printTriangle()

# o/p:
# * * * * 
# * * *
# * *
# *