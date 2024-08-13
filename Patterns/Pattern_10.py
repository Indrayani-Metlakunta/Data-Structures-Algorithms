# https://www.naukri.com/code360/problems/rotated-triangle_6573688?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nStarTriangle():
    N = int(input("Enter:"))
    for i in range(1,N+1):
        for j in range(i):
            print("*", end="")
        print()
    for i in range(1,N):
        for j in range(N-i):
            print("*", end="")
        print()
nStarTriangle()

# *
# **
# ***
# **
# *