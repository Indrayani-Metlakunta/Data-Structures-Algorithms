# https://www.geeksforgeeks.org/problems/triangle-number-1661428795/1

def printTriangle(self, N):
    for i in range(1,N+1):
        for j in range(i):
            print(i, end=" ")
        print() 

# o/p:
# 1
# 2 2
# 3 3 3
# 4 4 4 4