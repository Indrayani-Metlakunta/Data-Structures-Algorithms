
def printTriangle():
    N = int(input("Enter :"))
    for i in range(1,N+1):
        for j in range(N-i+1):
            print(j+1, end=" ")
        print()

printTriangle()