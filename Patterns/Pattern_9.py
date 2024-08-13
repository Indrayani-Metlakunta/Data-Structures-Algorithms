# https://www.naukri.com/code360/problems/star-diamond_6573686?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems

def nStarDiamond():
    N = int(input("Enter:"))
    # Upper part of the diamond
    for i in range(N):
        for j in range(N-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print('*', end="")
        print()
    
    # Lower part of the diamond
    for i in range(N):
        for j in range(i):
            print(" ", end="")
        for j in range(2*N-2*i-1):
            print('*', end="")
        print()

nStarDiamond()

# op:
#   *
#  ***
# *****
# *****
#  ***
#   *
