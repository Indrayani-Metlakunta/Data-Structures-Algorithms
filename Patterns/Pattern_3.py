def nTriangle():
    n = int(input("Enter: "))
    for i in range(1,n+1):
        for j in range(i):
            print(j+1, end=" ")
        print()
nTriangle()