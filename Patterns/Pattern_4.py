# https://www.geeksforgeeks.org/problems/triangle-number-1661428795/1

def printTriangle():
    N = int(input("Enter :"))
    for i in range(1,N+1):
        for j in range(i):
            print(i, end=" ")
        print() 

printTriangle()

# o/p:
# 1
# 2 2
# 3 3 3
# 4 4 4 4